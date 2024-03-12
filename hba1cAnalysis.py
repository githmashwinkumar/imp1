import os
import re
import fitz  # PyMuPDF
from datetime import datetime

def extract_collection_date_from_text(text):
    collection_date_pattern = r"Collection\s+On\s+(\d{1,2}/\d{1,2}/\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)"
    collection_date_matches = re.search(collection_date_pattern, text, re.IGNORECASE)
    if collection_date_matches:
        return datetime.strptime(collection_date_matches.group(1), "%d/%m/%Y %I:%M %p")
    return None

def extract_hba1c_from_text(text):
    hba1c_pattern = r"HbA1C\s+\(Whole Blood/HPLC\)\s+([\d.]+)\s+%"
    hba1c_matches = re.findall(hba1c_pattern, text)
    if hba1c_matches:
        return float(hba1c_matches[0])
    return None

def analyze_hba1c_trend(hba1c_values):
    if len(hba1c_values) < 2:
        print("Insufficient data to check trend.")
        return

    increasing_trend = all(hba1c_values[i] < hba1c_values[i+1] for i in range(len(hba1c_values) - 1))
    decreasing_trend = all(hba1c_values[i] > hba1c_values[i+1] for i in range(len(hba1c_values) - 1))

    if increasing_trend:
        print("Your Sugar readings are consistently increasing - Please book an appointment with a Doctor.")
    elif decreasing_trend:
        print("Your Sugar levels are in control - Keep it up.")
    else:
        print("Your Sugar readings are fluctuating. Consult your Doctor for further advice.")

def check_hba1c_trend(report_folder):
    collection_dates = []
    hba1c_values = []
    for filename in os.listdir(report_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(report_folder, filename)
            with fitz.open(pdf_path) as doc:
                text = ""
                for page in doc:
                    text += page.get_text()

            collection_date = extract_collection_date_from_text(text)
            hba1c_value = extract_hba1c_from_text(text)
            if collection_date and hba1c_value:
                collection_dates.append((collection_date, filename, hba1c_value))
            else:
                print(f"Skipping file '{filename}' due to missing collection date or HbA1c value.")

    # Sort collection dates
    sorted_collection_dates = sorted(collection_dates, key=lambda x: x[0])

    # Extract HbA1c readings
    for collection_date, filename, hba1c_value in sorted_collection_dates:
        print(f"Collection Date: {collection_date.strftime('%d/%m/%Y %I:%M %p')}, Filename: {filename}, HbA1c: {hba1c_value}")

    # Extract HbA1c values for trend analysis
    hba1c_values = [hba1c_value for _, _, hba1c_value in sorted_collection_dates]

    # Analyze HbA1c trend
    analyze_hba1c_trend(hba1c_values)

check_hba1c_trend(r"D:\Newfolder\Per\Healthview\Reports\Sugar\Amaji")
