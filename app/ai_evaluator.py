import json
import logging
import os
import time
from groq import Groq
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)

# Initialize Groq client
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in your .env file.")

try:
    client = Groq(api_key=api_key)
except Exception as e:
    logger.error(f"Failed to initialize Groq client: {e}")
    raise


def evaluate_cv(cv_content, evaluation_prompt):
    """
    Evaluate CV content using Groq AI API.

    Args:
        cv_content (str): Markdown content of the CV
        evaluation_prompt (str): Prompt with evaluation criteria

    Returns:
        dict: Evaluation results with keys: educationalQualification, jobHistory, skillSet, score, justification
    """

    # Construct the full prompt
    full_prompt = f"""
{evaluation_prompt}

CV Content:
{cv_content}

Please respond in the following JSON format:
{{
  "educationalQualification": "",
  "jobHistory": "",
  "skillSet": "",
  "score": 0,
  "justification": ""
}}
"""

    max_retries = 3
    retry_count = 0

    while retry_count < max_retries:
        try:
            # Call Groq API with streaming to match your requirements
            # Note: Using a currently supported model on Groq
            completion = client.chat.completions.create(
                model="openai/gpt-oss-120b",  # Using a currently supported Groq model
                messages=[
                    {
                        "role": "user",
                        "content": full_prompt,
                    }
                ],
                temperature=1,  # Match your specified temperature
                max_completion_tokens=8192,
                top_p=1,
                stream=True,  # Enable streaming as per your request
                stop=None
            )

            # Collect the streamed response
            response_text = ""
            for chunk in completion:
                content = chunk.choices[0].delta.content
                if content:
                    response_text += content

            # Parse the JSON response
            try:
                result = json.loads(response_text)

                # Validate required fields
                required_fields = ["educationalQualification", "jobHistory", "skillSet", "score", "justification"]
                for field in required_fields:
                    if field not in result:
                        raise ValueError(f"Missing required field: {field}")

                # Ensure score is a number between 0 and 100
                score = result["score"]
                if isinstance(score, str):
                    score = float(score) if '.' in score else int(score)
                elif not isinstance(score, (int, float)):
                    score = 0

                result["score"] = max(0, min(100, score))  # Clamp score between 0 and 100

                return result

            except json.JSONDecodeError as e:
                logger.error(f"Failed to decode JSON response: {e}")
                logger.debug(f"Response text: {response_text}")
                raise
            except ValueError as e:
                logger.error(f"Validation error in response: {e}")
                logger.debug(f"Response: {result}")
                raise
                
        except Exception as e:
            logger.error(f"Error calling Groq API (attempt {retry_count + 1}): {str(e)}")
            retry_count += 1
            
            if retry_count >= max_retries:
                # Return default error result after max retries
                return {
                    "educationalQualification": "Error processing",
                    "jobHistory": "Error processing", 
                    "skillSet": "Error processing",
                    "score": 0,
                    "justification": f"API Error after {max_retries} attempts: {str(e)}"
                }
            
            # Wait before retrying (exponential backoff)
            time.sleep(2 ** retry_count)