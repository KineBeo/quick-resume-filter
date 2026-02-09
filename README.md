# AI-Powered CV Screening Tool

A lightweight Python application that uses Groq LLM API to evaluate CVs and generate structured results in CSV format.

## 🚀 Features

- Reads PDF CV files from a specified folder
- Converts PDFs to Markdown for better LLM readability
- Evaluates CVs using Groq AI based on job role requirements
- Generates structured evaluation results in CSV format
- Dynamic evaluation criteria based on folder name (job role)

## 📋 Prerequisites

- Python 3.8+
- Groq API Key (get one at [https://console.groq.com/keys](https://console.groq.com/keys))

## 🛠️ Installation

1. Clone or download this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy the example environment file:
```bash
cp .env.example .env
```

4. Add your Groq API key to the `.env` file:
```bash
GROQ_API_KEY=your_actual_api_key_here
```

## 📁 Project Structure

```
app/
├── main.py              # Main application entry point
├── pdf_parser.py        # Converts PDFs to Markdown
├── ai_evaluator.py      # Evaluates CVs using Groq API
├── csv_writer.py        # Writes results to CSV
├── prompt_builder.py    # Builds dynamic evaluation prompts
└── config.py            # Configuration constants
```

## 🚀 Usage

Run the application with a folder containing CVs:

```bash
python app/main.py --folder "/path/to/cv/folder" --output "results.csv"
```

The folder name will be used as the job role for evaluation criteria. For example:
- `/cv_data/junior full stack developer/` → Evaluates CVs for "junior full stack developer" role

## 📊 Output Format

The results are saved in CSV format with the following columns:

| Column | Description |
|--------|-------------|
| output | Filename of the CV |
| educationalQualification | Summary of educational qualifications |
| jobHistory | Summary of job history and experience |
| skillSet | Extracted skills relevant to the role |
| score | Numeric score (0-100) indicating suitability |
| justification | Explanation for the score |

## ⚙️ Configuration

The application uses the following configuration:

- **Model**: llama-3.1-8b-instant (currently supported Groq model)
- **Temperature**: 1.0 (as specified for creativity)
- **Retry Logic**: Up to 3 attempts for API calls
- **Scoring Range**: 0-100 based on role relevance
- **Streaming**: Enabled for real-time response processing

## 🧠 Evaluation Logic

The AI evaluator dynamically generates evaluation criteria based on the job role name. It considers:

- Educational qualifications relevant to the role
- Job history and experience
- Technical and soft skills
- Overall fit for the position
- Realistic expectations for the role level

## 📊 Dashboard

The application now includes a Streamlit dashboard to visualize the results:

1. Run the dashboard:
```bash
streamlit run dashboard.py
```

2. The dashboard provides:
- Interactive candidate rankings
- Score distribution visualization
- Pass rate by level
- Detailed candidate information
- Filtering options by level, pass status, and score range
- Top candidates overview

## 📝 Notes

- The application automatically infers evaluation criteria from the folder name
- Scores are normalized between 0-100 to ensure consistency
- Error handling is implemented for PDF parsing and API failures
- UTF-8 encoding is used for proper character support