# Content-Differentiator

A **FastAPI-powered** web app that compares text differences between two columns from an uploaded file. It **highlights** removed text in **🟥 red (strike-through)** and added text in **🟩 green** to make changes easily visible! 📊  

🔥 **Features:**  
✅ Upload `.csv`, `.xlsx`, or `.xls` files.  
✅ Preview the uploaded file before processing.  
✅ Select any two columns to compare.  
✅ Get a downloadable **Excel file** 📂 with color-coded differences.  
✅ **Beautiful UI** 🎨 with Bootstrap & smooth animations.  
✅ 🚀 **FastAPI** backend with **async processing** for speed.  
✅ **Loading animations** & **progress bar** for better UX.  

---

## 🌟 Live Demo (GIF)  

![Demo](https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif)  
*(Replace with your actual demo GIF/video)*  

---

## 🛠 Technologies Used  

| **Tech**   | **Description**  |
|------------|----------------|
| ⚡ FastAPI  | Backend API   |
| 🐍 Python  | Core language  |
| 📊 Pandas  | Data processing  |
| 🎨 Bootstrap  | Frontend styling  |
| 🖍 xlsxwriter  | Excel formatting  |
| 🔄 difflib  | Text comparison  |

## 🚀 Installation & Setup  

### **🔧 Prerequisites:** 
Ensure you have Python 3.8+ installed on your system.

### Steps to Run Locally
### **📥 Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
📦 Install Dependencies:
   pip install -r requirements.txt
   
▶ Run the Application:
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


