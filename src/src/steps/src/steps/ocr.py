import pdfplumber

def ocr_pdf(pdf_path: str) -> str:
    """
    Baseline extraction for text-based PDFs.
    For scanned PDFs, extend with Tesseract or a cloud OCR provider.
    """
    text_parts = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text_parts.append(page.extract_text() or "")
    return "\n".join(text_parts).strip()
