import csv
import logging
from pathlib import Path


def write_results_to_csv(results, output_file):
    """
    Write evaluation results to a CSV file.

    Args:
        results (list): List of evaluation results
        output_file (str): Path to output CSV file
    """
    logger = logging.getLogger(__name__)

    # ✅ UPDATED: add new columns based on new prompt
    fieldnames = [
        'output',
        'educationalQualification',
        'jobHistory',
        'skillSet',
        'level',          # NEW
        'score',
        'pass',           # NEW
        'justification'
    ]

    try:
        # Write results to CSV
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write each result as a row
            for result in results:
                row = {}

                for field in fieldnames:
                    # Get value safely
                    value = result.get(field, '')

                    # Handle None values
                    if value is None:
                        value = ''

                    # ✅ IMPORTANT: normalize boolean pass -> string
                    if field == "pass":
                        if isinstance(value, bool):
                            value = "true" if value else "false"

                    # Convert to string if not already
                    if not isinstance(value, str):
                        value = str(value)

                    row[field] = value

                writer.writerow(row)

        logger.info(f"Successfully wrote {len(results)} results to {output_file}")

    except Exception as e:
        logger.error(f"Error writing results to CSV: {str(e)}")
        raise
