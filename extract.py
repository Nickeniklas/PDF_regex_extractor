import pdfplumber
import re

def extract_licenseplates(file_path):
    """ Extract license plates from a given PDF file. License plate fromat XYZ - 123"""
    plates = []
    try:
        with pdfplumber.open(f"./data/{file_path}") as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    # Normalize spacing and handle different dash types
                    text = text.replace("\n", " ")
                    plates.extend(re.findall(r"[A-Z]{3}[-–—]?\d{3}", text))
    except Exception as e:
        print("failed to extract.", e)
    print(f"Found {len(plates)} license plates:")
    return plates

if __name__ == "__main__":
    # extract license plates from this file
    file_path = "license_plates.pdf"
    plates = extract_licenseplates(file_path)
    if plates:
        print(plates)