# Content-Differentiator

## Overview
This project is a web-based application that allows users to upload spreadsheet files (CSV, XLSX, XLS) and compare the differences between two selected text columns. The application highlights differences in sentences using color-coded text and allows users to download the processed results.

## Features
- Upload and preview CSV, XLSX, and XLS files.
- Select two columns for text comparison.
- Detect differences in text using color-coded highlights.
- Download the processed file as an Excel document.
- User-friendly web interface built with Bootstrap.
- API backend using FastAPI.
- Supports CORS for cross-origin requests.

## Technologies Used
- **Backend:** FastAPI
- **Frontend:** HTML, Bootstrap, JavaScript
- **Libraries:** Pandas, difflib, xlsxwriter
- **Server:** Uvicorn

## Installation
### Prerequisites
Ensure you have Python 3.8+ installed on your system.

### Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
5. Open `index.html` in a browser or use a local server to view the front end.

## API Endpoints
### 1. Upload File and Preview
**Endpoint:** `POST /preview/`
- **Description:** Uploads a file and returns a preview of the data.
- **Payload:** Multipart file upload
- **Response:** JSON with filename and preview data.

### 2. Compare Columns and Generate Difference Report
**Endpoint:** `POST /content-difference/`
- **Description:** Compares two selected columns and returns a downloadable Excel file with color-coded differences.
- **Payload:**
  ```json
  {
    "file": "uploaded_file.xlsx",
    "column1": "Column A",
    "column2": "Column B"
  }
  ```
- **Response:** File download link (`final_output.xlsx`)

## Usage
1. Upload a CSV or Excel file.
2. Select two text-based columns for comparison.
3. Click "Compare & Download" to process the file.
4. Download the resulting Excel file with highlighted differences.

## Contributing
Feel free to fork the project, create feature branches, and submit pull requests. Contributions are welcome!

## Contact
For any issues or suggestions, please create an issue on the GitHub repository or contact the developer.

---
Made with ❤️ using FastAPI and Bootstrap.


