import pdfplumber
import re

plates = []

with pdfplumber.open("sample_data.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            # Normalize spacing and handle different dash types
            text = text.replace("\n", " ")
            plates.extend(re.findall(r"[A-Z]{3}[-–—]?\d{3}", text))

print(f"Found {len(plates)} license plates:")
print(plates)
