# loader.py
from pathlib import Path
from typing import List
from PyPDF2 import PdfReader

def load_pdf(file_path: str) -> str:
    """Load PDF and return its text."""
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def load_txt(file_path: str) -> str:
    """Load TXT file and return its text."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()