import os
import re
from pdfminer.high_level import extract_text

def extract_hba1c_and_collection_on(pdf_path):
    # Extract text from the PDF
    pdf_text = extract_text(pdf_path)

    # Use a regular expression to search for the HbA1C value
    hba1c_match = re.search(r'HbA1C[^0-9]*(\d+\.\d+)', pdf_text, re.IGNORECASE)

    hba1c_value = None

    if hba1c_match:
        hba1c_value = hba1c_match.group(1)

    # Use regex to search for the Collection On date
    collection_on_match = re.search(r'Collection\s*On[^0-9]*([\d\/]+\s*[\d:]+\s*[APMapm]+)', pdf_text, re.IGNORECASE)

    collection_on_date = None

    if collection_on_match:
        # Fetch the value from one line above
        collection_on_line = collection_on_match.group(0)
        collection_on_date_match = re.search(r'(\d+/\d+/\d+\s*[\d:]+\s*[APMapm]+)', collection_on_line)
        collection_on_date = collection_on_date_match.group(1).strip() if collection_on_date_match else None

    return hba1c_value, collection_on_date

def process_files_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory_path, filename)
            hba1c_value, collection_on_date = extract_hba1c_and_collection_on(pdf_path)

            if hba1c_value:
                print(f"The HbA1C value in {filename} is: {hba1c_value}")
            else:
                print(f"No HbA1C value found in {filename}")

            if collection_on_date:
                print(f"The Collection On date in {filename} is: {collection_on_date}")
            else:
                print(f"No Collection On date found in {filename}")

# Specify the directory containing your PDF files
pdf_directory = "D:\\Newfolder\\Per\\Healthview\\Reports\\Sugar\\Ashwin"
process_files_in_directory(pdf_directory)
