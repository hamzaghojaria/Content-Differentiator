from fastapi import UploadFile, HTTPException
import pandas as pd
import difflib
import xlsxwriter
from difflib import SequenceMatcher

def read_file(file: UploadFile):
    """Function to read CSV, XLSX, and XLS files into a Pandas DataFrame."""
    try:
        if file.filename.endswith(".csv"):
            df = pd.read_csv(file.file)
        elif file.filename.endswith(".xlsx"):
            df = pd.read_excel(file.file, engine="openpyxl")
        elif file.filename.endswith(".xls"):
            df = pd.read_excel(file.file, engine="xlrd")
        else:
            raise HTTPException(status_code=400, detail="Invalid file format. Only .xls, .xlsx, and .csv are allowed.")
        return df
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    



def color_diff(col1, col2):
    diff = difflib.ndiff(col1.split(), col2.split())
    formatted_diff = []
    
    for word in diff:
        if word.startswith('- '):
            formatted_diff.append(f'-{word[2:]}')
        elif word.startswith('+ '):
            formatted_diff.append(f'+{word[2:]}')
        elif word.startswith('  '):
            formatted_diff.append(word[2:])
    
    return ' '.join(formatted_diff)



def color_code_sentences(df, sentence_column, output_file):
    # Create a new Excel writer object using xlsxwriter
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        # Define formats for red, green, and black text
        red_format = workbook.add_format({'font_color': 'red', 'font_strikeout': True})
        green_format = workbook.add_format({'font_color': 'green'})
        black_format = workbook.add_format({'font_color': 'black'})

        # Iterate over the rows in the DataFrame
        for row_num, (index, row) in enumerate(df.iterrows(), start=1):
            # Write all columns except the sentence column
            for col_num, value in enumerate(row):
                if df.columns[col_num] != sentence_column:
                    worksheet.write(row_num, col_num, value)

            # Process the sentences column
            sentence = row[sentence_column]
            words = sentence.split()
            formatted_sentence = []

            for word in words:
                if word.startswith('-'):
                    formatted_sentence.extend([red_format, word[1:] + ' '])
                elif word.startswith('+'):
                    formatted_sentence.extend([green_format, word[1:] + ' '])
                else:
                    formatted_sentence.extend([black_format, word + ' '])

            # Find the column index of the sentence column
            sentence_col_idx = df.columns.get_loc(sentence_column)
            worksheet.write_rich_string(row_num, sentence_col_idx, *formatted_sentence)

            # Call the function with your DataFrame, the column to format, and the output file
        

def similarity_ratio(a, b):
    return SequenceMatcher(None, str(a), str(b)).ratio()  # Ensure text is string