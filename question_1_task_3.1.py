import collections
import csv
import re

# Function declaration to find the correct path
def readFile(filePath):
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
    txtFilePath = r'D:\assgn\group-assignment-python-code\outputtxt.txt'  # use raw string
    csvPath = r'D:\assgn\group-assignment-python-code\top30CommonWords.csv'  # use raw string
    #call the above functions    
    text = readFile(txtFilePath)
    
    wordCounts = countWords(text)
    
    topCommonWords = getTopCommonWords(wordCounts, 30)
    
    saveDataCsvFile(csvPath, topCommonWords)
    print(f'Top 30 common words saved to {csvPath}')

# calling the main function
if __name__ == '__main__':
    main()
