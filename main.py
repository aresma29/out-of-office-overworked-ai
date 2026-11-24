from pathlib import Path

entry_path = Path(__file__).resolve().parent / "entry.txt"
print(entry_path.read_text(encoding="utf-8"))
