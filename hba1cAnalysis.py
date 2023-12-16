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
        hba1c_value = float(hba1c_match.group(1))

    # Use regex to search for the Collection On date
    collection_on_match = re.search(r'Collection\s*On[^0-9]*([\d\/]+\s*[\d:]+\s*[APMapm]+)', pdf_text, re.IGNORECASE)

    collection_on_date = None

    if collection_on_match:
        collection_on_date = collection_on_match.group(1).strip()

    return hba1c_value, collection_on_date

def analyze_hba1c_trend(hba1c_values):
    if all(hba1c is not None for hba1c in hba1c_values):
        if all(hba1c_values[i] <= hba1c_values[i + 1] for i in range(len(hba1c_values) - 1)):
            print("Sugar levels are consistently increasing - Please consult a Doctor")
        elif all(hba1c_values[i] >= hba1c_values[i + 1] for i in range(len(hba1c_values) - 1)):
            print("Your Sugar levels are within limits - Keep up the good control")
        else:
            print("Sugar levels are not consistently increasing or decreasing")
    else:
        print("Insufficient data to analyze the trend")

def process_files_in_directory(directory_path):
    hba1c_values = []

    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory_path, filename)
            hba1c_value, collection_on_date = extract_hba1c_and_collection_on(pdf_path)

            # if hba1c_value:
            #     print(f"The HbA1C value in {filename} is: {hba1c_value}")
            #     hba1c_values.append(hba1c_value)
            # else:
            #     print(f"No HbA1C value found in {filename}")
            #
            # if collection_on_date:
            #     print(f"The Collection On date in {filename} is: {collection_on_date}")
            # else:
            #     print(f"No Collection On date found in {filename}")

    analyze_hba1c_trend(hba1c_values)

# Specify the directory containing your PDF files
pdf_directory = "D:\\Newfolder\\Per\\Healthview\\Reports\\Sugar\\Ashwin"
process_files_in_directory(pdf_directory)
