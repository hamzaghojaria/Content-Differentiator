from fastapi import FastAPI
from fastapi import UploadFile, File
from fastapi.responses import FileResponse
import pandas as pd
import uvicorn
from Backend import functions as differ_proc
#import functions as differ_proc
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Form

app = FastAPI()

# Enable CORS for all domains (for testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/preview/")
async def upload_file(file: UploadFile = File(...)):
    """API to upload file and return a preview."""
    df = differ_proc.read_file(file)
    return {"filename": file.filename, "preview": df.head().to_dict(orient="records")}


@app.post("/content-difference/") #Validates multiple selected columns and returns filtered data.
async def differentiator(
    column1: str = Form(...),
    column2: str = Form(...),
    file: UploadFile = File(...)
):
    try:    
        
        df = differ_proc.read_file(file)

        if df.shape[0] < 1: #checking that the data frame should contain rows
            return {"Error": "File contains 0 rows." }

        if df.shape[0] >= 1:
            if column1 == column2:
                return {"Error": "Both the names of the columns are the same." }

            selected_columns_list = [column1,column2] # Convert string to list

            print(f"Received selected_columns: {selected_columns_list}")  # Debugging

            missing_columns = [col for col in selected_columns_list if col not in df.columns] # Validate Valid Columns
            if missing_columns:
                return {"Error":f"Invalid columns: {missing_columns}. Available columns: {df.columns.tolist()}"}

            filtered_df = df[selected_columns_list]
            filtered_df.fillna("NA", inplace=True)
            filtered_df.reset_index(drop=True,inplace=True)
            

        
            if filtered_df.shape[0] < 1:
                return {"Error":"Filtered file contains 0 rows." }

            if filtered_df.shape[0] >= 1:
                print(column1, column2)
                filtered_df['Similarity Ratio'] = filtered_df.apply(lambda row: differ_proc.similarity_ratio(row[column1], row[column2]), axis=1)
                filtered_df['Similarity Ratio'] = filtered_df['Similarity Ratio'].round(2)
                filtered_df['Content_Difference'] = filtered_df.apply(lambda row: differ_proc.color_diff(row[column1], row[column2]), axis=1)

                filtered_df.reset_index(drop=True,inplace=True)
                filtered_df.to_excel("output1.xlsx")
                
                file_path = os.path.abspath("final_output.xlsx")
                differ_proc.color_code_sentences(filtered_df, 'Content_Difference',file_path )
                if os.path.exists(file_path):
                    return FileResponse(file_path, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename="final_output.xlsx")
                else:
                    return {"Error": "File not found."}
                #make similarity socre
                #return filtered_df.to_dict(orient="records")

    except Exception as e:
            return { "An Error has occurred in main ": str(e)}



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)






                #Differ
                # diff_data = []
                # for i, (text1, text2) in enumerate(zip(filtered_df[column1], filtered_df[column2])):
                #     diff = "\n".join(difflib.ndiff(text1.split(), text2.split()))
                #     diff_data.append({"Row": i,"Column1_Text": text1, "Column2_Text": text2, "Differences": diff})
                # # Create a DataFrame with differences
                # diff_df = pd.DataFrame(diff_data)


                #compare
                # diff_data = []
                #d = difflib.Differ()
                # for i, (text1, text2) in enumerate(zip(filtered_df[column1], filtered_df[column2])):
                #    diff = " ".join(d.compare(text1.split(), text2.split())) 
                #    diff_data.append({"Row": i,"Column1_Text": text1, "Column2_Text": text2, "Differences": diff})
                # # Create a DataFrame with differences
                # diff_df = pd.DataFrame(diff_data)
