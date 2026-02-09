import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="CV Screening Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("🔍 AI-Powered CV Screening Dashboard")
st.markdown("---")

# Load the results CSV
@st.cache_data
def load_data():
    df = pd.read_csv('results.csv')

    # --- FIX 1: Normalize score column ---
    # Convert score to numeric safely
    df['score'] = pd.to_numeric(df['score'], errors='coerce')

    # Drop rows where score is invalid
    df = df.dropna(subset=['score'])

    # Ensure score is float
    df['score'] = df['score'].astype(float)

    # --- FIX 2: Normalize pass column ---
    # CSV writer saves pass as string -> convert back to boolean
    df['pass'] = (
        df['pass']
        .astype(str)
        .str.lower()
        .map({'true': True, 'false': False})
    )

    # --- FIX 3: Clean level column (avoid nan issues) ---
    if 'level' in df.columns:
        df['level'] = df['level'].fillna("unknown")

    return df


try:
    df = load_data()
    
    # Display basic statistics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="Total CVs Processed", value=len(df))
    
    with col2:
        passed_candidates = len(df[df['pass'] == True])
        st.metric(label="Candidates Passed", value=passed_candidates)
    
    with col3:
        avg_score = df['score'].mean()
        st.metric(label="Average Score", value=f"{avg_score:.1f}/100")
    
    with col4:
        highest_score = df['score'].max()
        st.metric(label="Highest Score", value=f"{highest_score}/100")
    
    st.markdown("---")
    
    # Filters
    st.sidebar.header("Filters")
    
    # Job level filter
    levels = ['All'] + sorted(df['level'].unique().tolist())
    selected_level = st.sidebar.selectbox("Select Level", options=levels, index=0)
    
    # Pass status filter
    pass_status = ['All', 'Passed', 'Not Passed']
    selected_pass = st.sidebar.selectbox("Pass Status", options=pass_status, index=0)
    
    # Score range filter
    min_score, max_score = int(df['score'].min()), int(df['score'].max())
    score_range = st.sidebar.slider("Score Range", min_value=min_score, max_value=max_score, 
                                   value=(min_score, max_score))
    
    # Apply filters
    filtered_df = df.copy()
    if selected_level != 'All':
        filtered_df = filtered_df[filtered_df['level'] == selected_level]
    
    if selected_pass == 'Passed':
        filtered_df = filtered_df[filtered_df['pass'] == True]
    elif selected_pass == 'Not Passed':
        filtered_df = filtered_df[filtered_df['pass'] == False]
    
    filtered_df = filtered_df[(filtered_df['score'] >= score_range[0]) & 
                             (filtered_df['score'] <= score_range[1])]
    
    # Display filtered dataframe
    st.subheader(f"Candidate Rankings ({len(filtered_df)} candidates)")
    
    # Sort by score descending
    filtered_df_sorted = filtered_df.sort_values(by='score', ascending=False)
    
    # Display table without color styling to avoid comparison errors
    display_df = filtered_df_sorted[['output', 'score', 'level', 'pass', 'justification']].copy()
    # Round scores for display
    display_df['score'] = display_df['score'].round(1)

    st.dataframe(display_df, height=400)
    
    # Charts
    st.markdown("---")
    st.subheader("Visual Analytics")
    
    # Create two columns for charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Score distribution histogram
        fig_hist = px.histogram(filtered_df, x='score', nbins=20, title="Score Distribution",
                               labels={'score': 'Score', 'count': 'Number of Candidates'})
        fig_hist.update_layout(showlegend=False)
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        # Pass rate by level
        if 'level' in filtered_df.columns:
            pass_rate_by_level = filtered_df.groupby('level').agg({
                'pass': lambda x: (x.sum() / len(x)) * 100,
                'output': 'count'
            }).reset_index()
            pass_rate_by_level.columns = ['Level', 'Pass Rate (%)', 'Total Candidates']
            
            fig_bar = px.bar(pass_rate_by_level, x='Level', y='Pass Rate (%)',
                            title="Pass Rate by Level",
                            text=[f'{rate:.1f}%' for rate in pass_rate_by_level['Pass Rate (%)']])
            st.plotly_chart(fig_bar, use_container_width=True)
    
    # Top candidates section
    st.markdown("---")
    st.subheader("Top Candidates")
    
    top_n = st.slider("Show top N candidates", min_value=1, max_value=min(10, len(filtered_df_sorted)), value=5)
    top_candidates = filtered_df_sorted.head(top_n)
    
    for idx, row in top_candidates.iterrows():
        with st.expander(f"📄 {row['output']} - Score: {row['score']}/100"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Educational Qualification:**")
                st.write(row['educationalQualification'])
                
                st.write("**Job History:**")
                st.write(row['jobHistory'])
            
            with col2:
                st.write("**Skills:**")
                st.write(row['skillSet'])
                
                st.write("**Justification:**")
                st.write(row['justification'])
    
    # Detailed view for individual candidate
    st.markdown("---")
    st.subheader("Candidate Details")
    
    selected_candidate = st.selectbox("Select a candidate to view details:", 
                                     options=filtered_df_sorted['output'].tolist())
    
    if selected_candidate:
        candidate_data = filtered_df_sorted[filtered_df_sorted['output'] == selected_candidate].iloc[0]
        
        st.markdown(f"### {selected_candidate}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(label="Score", value=f"{candidate_data['score']}/100", 
                     delta="Pass" if candidate_data['pass'] else "Don't Pass")
            st.write(f"**Level:** {candidate_data['level']}")
        
        with col2:
            if candidate_data['score'] >= 80:
                st.success("Strong Candidate")
            elif candidate_data['score'] >= 70:
                st.warning("Moderate Candidate")
            else:
                st.error("Weak Candidate")
        
        st.write("**Educational Qualification:**")
        st.info(candidate_data['educationalQualification'])
        
        st.write("**Job History:**")
        st.info(candidate_data['jobHistory'])
        
        st.write("**Skills:**")
        st.info(candidate_data['skillSet'])
        
        st.write("**Justification:**")
        if candidate_data['pass']:
            st.success(candidate_data['justification'])
        else:
            st.error(candidate_data['justification'])

except FileNotFoundError:
    st.error("❌ Results.csv file not found. Please run the CV screening application first.")
    st.info("Run: `python app/main.py --folder './your_folder' --output 'results.csv'`")
except Exception as e:
    st.error(f"❌ An error occurred while loading the data: {str(e)}")
    st.info("Make sure you have the required dependencies installed: `pip install streamlit pandas plotly`")