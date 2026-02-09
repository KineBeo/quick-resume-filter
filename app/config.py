"""
Configuration module for the CV screening application.
Contains constants and settings used across the application.
"""

import os
from pathlib import Path

# API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# File processing configuration
SUPPORTED_FILE_TYPES = ['.pdf']

# Default output settings
DEFAULT_OUTPUT_FILE = "cv_evaluation_results.csv"

# AI evaluation settings
AI_TEMPERATURE = 0.2  # Lower temperature for more consistent evaluations
MAX_RETRIES = 3       # Number of retry attempts for API calls

# Logging configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Application defaults
DEFAULT_MODEL_NAME = "llama3-8b-8192"

# Scoring thresholds (can be adjusted based on requirements)
SCORE_THRESHOLDS = {
    "excellent": (90, 100),
    "strong": (80, 89),
    "good": (70, 79),
    "fair": (60, 69),
    "marginal": (50, 59),
    "poor": (0, 49)
}