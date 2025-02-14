# Content-Differentiator

# Text Difference Checker

A FastAPI-based web application that allows users to compare the content of two selected columns from an uploaded Excel (`.xlsx`, `.xls`) or CSV (`.csv`) file and visualize differences. The application highlights removed text in red (strike-through) and added text in green. 

## Features

- Upload `.csv`, `.xlsx`, or `.xls` files.
- Preview the uploaded file.
- Select two columns for comparison.
- Highlight differences in content between the two columns.
- Download the processed file with color-coded differences.
- User-friendly front-end with Bootstrap UI.
- Progress bar and full-page loader animations for better UX.

## Technologies Used

- **Backend:** FastAPI, Pandas, difflib, xlsxwriter, CORS middleware
- **Frontend:** HTML, CSS (Bootstrap), JavaScript (Fetch API)
- **Server:** Uvicorn

## Installation

### Prerequisites

- Python 3.8 or later
- pip package manager

### Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/text-difference-checker.git
   cd text-difference-checker
