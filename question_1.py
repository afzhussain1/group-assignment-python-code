
import zipfile
import pandas as pd
import os
#take the column from the user
column_name = input("Please enter the column name to extract text from: ")
#paths and please change the paths according to your location thanks
zip_path = r'D:\assgn\group-assignment-python-code\csv_.zip'  # Path to the ZIP file
extracted_path = r'D:\assgn\group-assignment-python-code\csv_extracted'  # Directory for extracted files
output_txt_path = r'D:\assgn\group-assignment-python-code\outputtxt.txt'  # Path for the output text file

os.makedirs(extracted_path, exist_ok=True)

#  Extraction the zip files and the save them into extracted folder
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_path)

# empty array to collect the files
all_texts = []

#for loops to read the file
for root, dirs, files in os.walk(extracted_path):
    for file in files:
        if file.endswith('.csv'):  # Process only CSV files
            file_path = os.path.join(root, file)
            try:
                df = pd.read_csv(file_path)
                
                # Check if 'TEXT' column exists in the CSV file
                if column_name  in df.columns:
                    texts = df[column_name].dropna().tolist()  
                    all_texts.extend(texts)
                else:
                    print(f"Warning: {column_name} column is not found in path {file_path}")

            except pd.errors.EmptyDataError:
                print(f"Warning: {file_path} is empty file.")
            except pd.errors.ParserError:
                print(f"Warning: Errors in {file_path}. It may be corrupted.")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

# Check if any texts were collected
if all_texts:
    # Write collected texts into a text file
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        for text in all_texts:
            f.write(text + '\n')
    print(f'All texts have been saved to {output_txt_path}')
else:
    print('No texts were found to save.')




