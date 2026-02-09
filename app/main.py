import os
import argparse
import logging
from pathlib import Path
from pdf_parser import parse_pdf_to_markdown
from ai_evaluator import evaluate_cv
from csv_writer import write_results_to_csv
from prompt_builder import build_evaluation_prompt


def setup_logging():
    """Setup logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def main():
    """Main function to process CVs and evaluate them."""
    parser = argparse.ArgumentParser(description='AI-powered CV Screening Tool')
    parser.add_argument('--folder', type=str, required=True, help='Path to folder containing CVs')
    parser.add_argument('--output', type=str, default='results.csv', help='Output CSV file path')
    
    args = parser.parse_args()
    
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Validate input folder
    folder_path = Path(args.folder)
    if not folder_path.exists():
        logger.error(f"Folder does not exist: {args.folder}")
        return
    
    # Extract job role from folder name
    job_role = folder_path.name.replace('_', ' ').replace('-', ' ').strip()
    logger.info(f"Processing CVs for job role: '{job_role}'")
    
    # Build evaluation prompt based on job role
    evaluation_prompt = build_evaluation_prompt(job_role)
    
    # Find all PDF files in the folder
    pdf_files = list(folder_path.glob('*.pdf'))
    if not pdf_files:
        logger.warning(f"No PDF files found in {args.folder}")
        return
    
    logger.info(f"Found {len(pdf_files)} PDF files to process")
    
    results = []
    
    # Process each CV
    for pdf_file in pdf_files:
        logger.info(f"Processing {pdf_file.name}")
        
        try:
            # Parse PDF to Markdown
            markdown_content = parse_pdf_to_markdown(pdf_file)
            
            # Evaluate CV using AI
            evaluation_result = evaluate_cv(markdown_content, evaluation_prompt)
            
            # Add filename to result
            evaluation_result['output'] = pdf_file.name
            
            results.append(evaluation_result)
            
            logger.info(f"Completed processing {pdf_file.name}, score: {evaluation_result.get('score', 'N/A')}")
            
        except Exception as e:
            logger.error(f"Error processing {pdf_file.name}: {str(e)}")
            # Add error entry to results
            results.append({
                'output': pdf_file.name,
                'educationalQualification': 'Error processing',
                'jobHistory': 'Error processing',
                'skillSet': 'Error processing',
                'score': 0,
                'justification': f'Error: {str(e)}'
            })
    
    # Write results to CSV
    write_results_to_csv(results, args.output)
    logger.info(f"Results saved to {args.output}")


if __name__ == "__main__":
    main()