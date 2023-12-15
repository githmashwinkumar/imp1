import os
from pdfminer.high_level import extract_text

class LabDataObject:
    def __init__(self):
        self._dateoftest = None
        self._labResult = None

    @property
    def dateoftest(self):
        return self._dateoftest

    @property
    def labResult(self):
        return self._labResult

    @dateoftest.setter
    def dateoftest(self, value):
        self._dateoftest = value

    @labResult.setter
    def labResult(self, value):
        self._labResult = value

# Function to extract data from PDF and create LabDataObject instances
def extract_data_from_pdf(pdf_path):
    lab_data_list = []

    # Extract text from the PDF
    pdf_text = extract_text(pdf_path)

    # Split the text into lines
    lines = pdf_text.split('\n')

    # Assuming dateoftest is at the 52nd position and labResult is at the 77th position
    dateoftest = lines[51].strip() if len(lines) > 51 else None
    labResult = lines[76].strip() if len(lines) > 76 else None

    # Create LabDataObject instance
    lab_data = LabDataObject()
    lab_data.dateoftest = dateoftest
    lab_data.labResult = labResult

    # Append the LabDataObject to the list, excluding empty labResult
    if labResult:
        lab_data_list.append(lab_data)

    return lab_data_list

# Function to check if lab results are consistently increasing
def check_increasing_lab_results(across_files_lab_data):
    # Extract lab results from all files
    lab_results = [float(lab_data.labResult) for lab_data in across_files_lab_data if lab_data.labResult]

    # Check if the lab results are in increasing order
    increasing_order = all(lab_results[i] <= lab_results[i + 1] for i in range(len(lab_results) - 1))

    return increasing_order

# Directory containing PDF files
pdf_directory = 'D:\\Newfolder\\Per\\Healthview\\Reports\\Sugar\\Ashwin'

# Get a list of PDF files in the directory
pdf_files = [file for file in os.listdir(pdf_directory) if file.endswith('.pdf')]

# Accumulate lab data across all files
across_files_lab_data = []

# Iterate through each PDF file
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_directory, pdf_file)

    # Extract data from PDF and create LabDataObject instances
    lab_data_list = extract_data_from_pdf(pdf_path)

    # Accumulate lab data from each file
    across_files_lab_data.extend(lab_data_list)

# Check if lab results are consistently increasing across all files
increasing_order = check_increasing_lab_results(across_files_lab_data)

# Print the result message
if increasing_order:
    print("Sugar levels are consistently increasing - Please consult the doctor.")
else:
    print("Sugar levels are not consistently increasing!")
