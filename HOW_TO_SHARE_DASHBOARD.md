# Sharing the CV Screening Dashboard

## Option 1: Share the Interactive Dashboard (Recommended)

To share the interactive dashboard with others:

1. **Share these files:**
   - `dashboard.py` (the dashboard code)
   - `results.csv` (your processed data)
   - `dashboard_requirements.txt` (dependencies)

2. **Instructions for recipients:**
   ```bash
   # Install required packages
   pip install -r dashboard_requirements.txt
   
   # Run the dashboard
   streamlit run dashboard.py
   ```

## Option 2: Export Static Report

If you want to create a static report that preserves the visualizations:

1. **Install streamlit-nested-layout (optional enhancement):**
   ```bash
   pip install streamlit-nested-layout
   ```

2. **Take screenshots of the dashboard** while interacting with different filters

3. **Export the data:**
   - Use the "Download filtered data as CSV" button in the dashboard
   - Or export specific visualizations as images

## Option 3: Deploy Online (Advanced)

You can deploy the dashboard online using:
- Streamlit Cloud
- Heroku with Streamlit
- AWS/GCP

For Streamlit Cloud:
1. Put the code in a GitHub repository
2. Connect to Streamlit Cloud
3. Share the public URL

## Files to Share

When sharing with others, include:
- `dashboard.py` - The dashboard application
- `results.csv` - Your evaluation results  
- `dashboard_requirements.txt` - Required Python packages
- This README file - Instructions for running

The recipients will be able to run the exact same interactive dashboard with your data and see all the visualizations and filtering capabilities.