from transformers import AutoTokenizer
from collections import Counter

def rTextFile(filePath):
    with open(filePath, 'r', encoding='utf-8') as file:
        return file.read()

def cUniqueTokens(text, modelName='bert-base-uncased'):
    tokenizer = AutoTokenizer.from_pretrained(modelName)
    tokens = tokenizer.tokenize(text)
    return Counter(tokens)

def getTopTokens(tokenCounts, n=30):
    return tokenCounts.most_common(n)

def main_funtion():
    # file path
    inFilePath = r'C:\Users\Speed\Documents\group-assignment\textfile1.txt'  # Use raw string
    
    # Calling the function
    text = rTextFile(inFilePath)
    
    tokenCounts = cUniqueTokens(text)
    
    topTokens = getTopTokens(tokenCounts, 30)
    
    print(f'Get Top 30 tokens: {topTokens}')
#main function call
if __name__ == '__main__':
    main_funtion()
