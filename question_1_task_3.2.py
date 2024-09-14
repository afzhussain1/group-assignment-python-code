from transformers import AutoTokenizer
from collections import Counter
import os

def rTextFile(filePath):
    if not os.path.isfile(filePath):
        raise FileNotFoundError(f"The file at that {filePath} does not exist.")
    
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            content = file.read()
    except IOError as e:
        raise IOError(f"An error: {e}")
    
    if not content:
        raise ValueError("The file is empty.")
    
    return content

def cUniqueTokens(text, modelName='bert-base-uncased'):
    # to handle the exaption
    try:
        tokenizer = AutoTokenizer.from_pretrained(modelName)
    except Exception as e:
        raise RuntimeError(f"An error occurred while loading the tokenizer: {e}")
    
    tokens = tokenizer.tokenize(text)
    return Counter(tokens)

def getTopTokens(tokenCounts, n=30):
    return tokenCounts.most_common(n)
# Calling the function

def main_function():
    #file path
    inFilePath = r'D:\assgn\group-assignment-python-code\outputtxt.txt' 
    
    try:
        text = rTextFile(inFilePath)
        tokenCounts = cUniqueTokens(text)
        topTokens = getTopTokens(tokenCounts, 30)
        print(f'Get Top 30 tokens: {topTokens}')
    except (FileNotFoundError, IOError, ValueError, RuntimeError) as e:
        print(f"An error occurred: {e}")

# Main function call
if __name__ == '__main__':
    main_function()
