import os
import re
from pdfminer.high_level import extract_text


# Function to extract HbA1c value from PDF
def extract_hba1c_value(pdf_path):
    # Extract text from the PDF
    pdf_text = extract_text(pdf_path)

    # Use a regular expression to search for the HbA1c value
    hba1c_match = re.search(r'HbA1C\s*\(Whole Blood/HPLC\)\s*([\d.]+)', pdf_text, re.IGNORECASE)

    if hba1c_match:
        hba1c_value = hba1c_match.group(1)
        # Convert the value to float if it contains valid numeric characters
        try:
            return float(hba1c_value)
        except ValueError:
            pass

    return None


# Directory containing PDF files
pdf_directory = 'D:\\Newfolder\\Per\\Healthview\\Reports\\Sugar\\Ashwin'

# Get a list of PDF files in the directory
pdf_files = [file for file in os.listdir(pdf_directory) if file.endswith('.pdf')]

# Iterate through each PDF file
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_directory, pdf_file)

    # Extract HbA1c value from the PDF
    hba1c_value = extract_hba1c_value(pdf_path)

    # Print the result
    if hba1c_value is not None:
        print(f"The HbA1c value in {pdf_file} is: {hba1c_value}")
    else:
        print(f"No HbA1c value found in {pdf_file}")
