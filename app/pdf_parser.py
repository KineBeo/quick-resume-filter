import fitz  # PyMuPDF
import logging
from pathlib import Path


def parse_pdf_to_markdown(pdf_path):
    """
    Convert PDF content to Markdown-style plain text.

    Args:
        pdf_path (Path): Path to the PDF file

    Returns:
        str: Markdown-style text content of the PDF
    """
    logger = logging.getLogger(__name__)

    try:
        # Open the PDF file - ensure proper handling of special characters in path
        doc = fitz.open(str(pdf_path))
        text_content = []

        # Extract text from each page
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text()

            # Add page content with markdown-style formatting
            if text.strip():  # Only add non-empty pages
                # Attempt to identify headers based on font size or position
                try:
                    blocks = page.get_text("dict")["blocks"]

                    page_text = ""
                    for block in blocks:
                        if "lines" in block:  # Text block
                            for line in block["lines"]:
                                line_text = ""
                                for span in line["spans"]:
                                    line_text += span["text"]

                                # Simple heuristic to detect headers based on font size
                                # Usually headers are larger fonts
                                if len(line_text.strip()) > 0:
                                    # Check if this looks like a header (larger font size)
                                    span_font_size = block["lines"][0][0]["size"] if block["lines"] and block["lines"][0] and block["lines"][0][0] else 12

                                    # If font size is significantly larger than normal (12pt), treat as header
                                    if span_font_size > 14:
                                        page_text += f"\n# {line_text}\n"
                                    else:
                                        page_text += f"{line_text}\n"

                    text_content.append(page_text)
                except:
                    # Fallback: just get the raw text if block parsing fails
                    text_content.append(text)

        doc.close()

        # Join all page content
        full_text = "\n".join(text_content)

        # Clean up extra whitespace
        full_text = "\n".join([line.strip() for line in full_text.split("\n") if line.strip()])

        return full_text

    except Exception as e:
        logger.error(f"Error parsing PDF {pdf_path}: {str(e)}")
        # Return empty string as fallback
        return ""