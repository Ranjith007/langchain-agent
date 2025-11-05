# tools/file_reader.py
from pathlib import Path
import os

BASE_DIR = Path.cwd()  # you can change this to a `data/` directory for safety

def read_file(path: str, max_chars: int = 10000) -> str:
    candidate = (BASE_DIR / path).resolve()
    if not str(candidate).startswith(str(BASE_DIR.resolve())):
        return "Error: Path outside allowed directory."
    if not candidate.exists():
        return f"Error: File not found: {path}"
    try:
        with open(candidate, "r", encoding="utf-8") as f:
            return f.read(max_chars)
    except Exception as e:
        return f"Read error: {e}"
