# Content-Differentiator

A **FastAPI-powered** web app that compares text differences between two columns from an uploaded file. It **highlights** removed text in **🟥 red (strike-through)** and added text in **🟩 green** to make changes easily visible! 📊  

## 🔥 Features:
✅ Upload `.csv`, `.xlsx`, or `.xls` files.  
✅ Preview the uploaded file before processing.  
✅ Select any two columns to compare.  
✅ Get a downloadable **Excel file** 📂 with color-coded differences.  

---

## 🛠 How It Works
* Upload your file 📂
* Select two columns for comparison 📊
* Click "Compare & Download" 🚀
* Download the Excel file with differences marked! ✅

### 📌 Text Highlighting:
* ❌ Deleted text → 🟥 Red (Strike-through)
* ✅ Added text → 🟩 Green
* 🔽 Screenshots:
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
```bash
Ensure you have Python 3.8+ installed on your system.
```
### **💻 Steps to Run Locally:**

### 📥 Clone the Repository
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

## Contributing
Feel free to fork the project, create feature branches, and submit pull requests. Contributions are welcome!

## Contact
For any issues or suggestions, please create an issue on the GitHub repository or contact the developer.

---
Made with ❤️ using FastAPI and Bootstrap.
