import argparse
from pathlib import Path
from src.steps.ocr import ocr_pdf
from src.steps.chunk import chunk_text
from src.steps.extract import extract_fields
from src.steps.validate import validate_output
from src.utils.io import write_json

def run(input_path: str, out_dir: str):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    text = ocr_pdf(input_path)
    chunks = chunk_text(text, max_chars=1200)

    extracted = extract_fields(chunks)
    validated = validate_output(extracted)

    write_json(validated, out_dir / "output.json")
    print(f"✅ Done. Wrote: {out_dir / 'output.json'}")

if _name_ == "_main_":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    run(args.input, args.out)
