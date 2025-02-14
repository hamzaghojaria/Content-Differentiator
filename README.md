# Content-Differentiator

A **FastAPI-powered** web app that compares text differences between two columns from an uploaded file. It **highlights** removed text in **🟥 red (strike-through)** and added text in **🟩 green** to make changes easily visible! 📊  

🔥 **Features:**  
✅ Upload `.csv`, `.xlsx`, or `.xls` files.  
✅ Preview the uploaded file before processing.  
✅ Select any two columns to compare.  
✅ Get a downloadable **Excel file** 📂 with color-coded differences.  
✅ **Beautiful UI** 🎨 with Bootstrap & smooth animations.  

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
### 💻 Create a virtual environment and activate it: 
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   
### 📦 Install Dependencies:    
   ```bash
   pip install -r requirements.txt
   ```
### ▶ Run the Application: 
   ```bash
   uvicorn main:app --reload
   ```
### 🌐 Open Frontend:
```bash
Simply open index.html in your browser! 🌍
```

## 🔗 API Endpoints
* 🟢 Upload File & Preview (POST /preview/)
* 📂 Request: Upload a .csv / .xlsx / .xls file.
* 📊 Response: Returns a preview of the first few rows.

🟢 Compare Columns & Download (POST /content-difference/)
📂 Request:
* file → Uploaded file
* column1 → First column to compare
* column2 → Second column to compare
📊 Response: Returns a downloadable Excel file (final_output.xlsx) with highlighted differences! 🎉

🛠 How It Works
🔹 Upload your file 📂
🔹 Select two columns for comparison 📊
🔹 Click "Compare & Download" 🚀
🔹 Download Excel file with differences marked! ✅

📌 Text Highlighting:

❌ Deleted text → 🟥 Red (Strike-through)
✅ Added text → 🟩 Green

🎨 UI Highlights
✨ Bootstrap-powered UI for smooth interactions!
⏳ Loading animations & progress bar for better feedback!
📥 Easy file upload & instant preview!

🔽 Screenshots:

## Contributing
Feel free to fork the project, create feature branches, and submit pull requests. Contributions are welcome!

## Contact
For any issues or suggestions, please create an issue on the GitHub repository or contact the developer.

---
Made with ❤️ using FastAPI and Bootstrap.


