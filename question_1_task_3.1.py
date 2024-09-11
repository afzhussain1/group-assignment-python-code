import collections
import csv
import re
import os

# Function declaration to find the correct path
def readFile(filePath):
     if not os.path.isfile(filePath):
        raise FileNotFoundError(f"File not found: {filePath}")
     with open(filePath, 'r', encoding='utf-8') as file:
        return file.read()

# Function declaration to count the repeated words
def countWords(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return collections.Counter(words)

def getTopCommonWords(wordCounts, n=30):
    return wordCounts.most_common(n)

# Function to store the data in CSV file in column way
def saveDataCsvFile(filePath, commonWords):
    with open(filePath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Count'])
        writer.writerows(commonWords)

# Main function to call the all above function
def main():
    txtFilePath = r'D:\assgn\group-assignment-python-code\outputtxt.txt'  
    outCsvPath = r'D:\assgn\group-assignment-python-code\top30CommonWords.csv'  
    #callin the above functions
    try:
        text = readFile(txtFilePath)
        
        wordCounts = countWords(text)
        
        topCommonWords = getTopCommonWords(wordCounts, 30)
        
        saveDataCsvFile(outCsvPath, topCommonWords)
        print(f'Top 30 common words saved to {outCsvPath}')
    
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Execute the main function
if __name__ == '__main__':
    main()
