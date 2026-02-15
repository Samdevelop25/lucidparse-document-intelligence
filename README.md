# LucidParse — AI Document Intelligence

## Overview
LucidParse is an AI-assisted document intelligence pipeline that converts PDFs (including scanned docs) into reliable structured outputs.

*Goal:* Extract tables/fields from PDFs into clean JSON/CSV with validation and confidence scoring.  
*Stack:* Python, OCR, embeddings, retrieval-style extraction, deterministic validation  
*Focus:* accuracy, latency/cost tradeoffs, and reducing unreliable outputs via post-processing guardrails

---

## Problem
Organizations store critical information in PDFs (invoices, statements, forms), but PDFs are difficult to reliably convert into structured data.  
Common issues include inconsistent layouts, OCR noise, and extraction errors that break downstream analytics.

---

## Solution Architecture

PDF → OCR → Text Cleanup → Chunking → Embeddings → Relevant Context Retrieval → Extraction → Validation → Structured Output (JSON/CSV)

### Reliability Guardrails
- schema-based validation (required fields, types, ranges)
- normalization (dates, currency, IDs)
- confidence scoring & rule-based checks
- failure modes logged for review

---

## Repository Structure
- src/ core pipeline code
- data/sample_pdfs/ small sample docs (no sensitive data)
- data/sample_outputs/ extracted structured outputs
- docs/ architecture + data dictionary

---

## How to run (local)
```bash
pip install -r requirements.txt
python src/run_pipeline.py --input data/sample_pdfs/sample_invoice.pdf --out data/sample_outputs/
