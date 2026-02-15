import re

def extract_fields(chunks):
    joined = "\n".join(chunks)

    invoice_number = None
    m = re.search(r"(Invoice\s*#|Invoice\s*No\.?)\s*[:\-]?\s*([A-Z0-9\-]+)", joined, re.IGNORECASE)
    if m:
        invoice_number = m.group(2)

    invoice_date = None
    m = re.search(r"(Date)\s*[:\-]?\s*([0-9]{1,2}[\/\-][0-9]{1,2}[\/\-][0-9]{2,4})", joined, re.IGNORECASE)
    if m:
        invoice_date = m.group(2)

    total_amount = None
    m = re.search(r"(Total)\s*[:\-]?\s*\$?\s*([0-9,]+\.\d{2})", joined, re.IGNORECASE)
    if m:
        total_amount = m.group(2)

    return {
        "invoice_number": invoice_number,
        "invoice_date": invoice_date,
        "total_amount": total_amount,
        "raw_preview": joined[:500]
    }
