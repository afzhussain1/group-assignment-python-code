
import spacy
import scispacy
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import os

# Function to read text from a file
def loadText(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        raise IOError(f"Error reading the file at {file_path}: {e}")

# Function to check SpaCy and SciSpaCy models
def checkSpacyScispacy():
    try:
        nlpSciFile = spacy.load('en_core_sci_sm')
        print("Loaded en_core_sci_sm successfully.")
        
        nlpBc5cdrFile = spacy.load('en_ner_bc5cdr_md')
        print("Loaded en_ner_bc5cdr_md successfully.")
        
        return nlpSciFile, nlpBc5cdrFile
    except Exception as e:
        print(f"Error loading the SpaCy/scispaCy models: {e}")
        return None, None

# Function to load Hugging Face Transformers and BioBERT
def transformersBiobert(text):
    try:
        tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
        model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
        nlp = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")
        
        entities = nlp(text)
        if entities:
            print("BioBERT entities:", entities)
        else:
            print("No entities found by BioBERT.")
        return entities
    except Exception as e:
        print(f"Error loading Hugging Face and BioBERT models: {e}")
        return None

def main():
    # Path to your text file
    file_path = 'D:/group-assignment-python-code/outputtxt.txt'
    
    try:
        text = loadText(file_path)
        print(f"Loaded text from {file_path}.")
    except (FileNotFoundError, IOError) as e:
        print(e)
        return

    # Check SpaCy models
    nlpSciFile, nlpBc5cdrFile = checkSpacyScispacy()
    
    if nlpSciFile and nlpBc5cdrFile:
        print("Processing text with SpaCy models...")
        doc_sci_sm = nlpSciFile(text)
        doc_bc5cdr = nlpBc5cdrFile(text)
        
        if doc_sci_sm.ents:
            print("Entities from en_core_sci_sm:")
            for ent in doc_sci_sm.ents:
                print(ent.text, ent.label_)
        else:
            print("No entities found by en_core_sci_sm.")
        
        if doc_bc5cdr.ents:
            print("Entities from en_ner_bc5cdr_md:")
            for ent in doc_bc5cdr.ents:
                print(ent.text, ent.label_)
        else:
            print("No entities found by en_ner_bc5cdr_md.")
    
    biobert_entities = transformersBiobert(text)
    if not biobert_entities:
        print("No entities found by BioBERT.")

if __name__ == "__main__":
    main()
