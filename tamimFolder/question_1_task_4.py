import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
from collections import Counter
import os

# function to read the txt file
def loadText(filePath):
    if not os.path.isfile(filePath):
        raise FileNotFoundError(f"The file at {filePath} does not exist.")
    try:
        with open(filePath, 'r') as file:
            return file.read()
    except Exception as e:
        raise IOError(f"Error reading the file at {filePath}: {e}")

# Extract model
def extractDisease(text, modelName):
    try:
        nlp = spacy.load(modelName)
    except Exception as e:
        raise RuntimeError(f"Error loading SpaCy model '{modelName}': {e}")
    
    try:
        doc = nlp(text)
    except Exception as e:
        raise RuntimeError(f"Error text with SpaCy model '{modelName}': {e}")
    
    diseases = [ent.text for ent in doc.ents if ent.label_ == 'DISEASE']
    drugs = [ent.text for ent in doc.ents if ent.label_ == 'DRUG']
    
    return diseases, drugs

# function biobert model
def extractBiobert(text):
    try:
        tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
        model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
        nlp = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")
    except Exception as e:
        raise RuntimeError(f"Error BioBERT model or tokenizer: {e}")
    
    try:
        entities = nlp(text)
    except Exception as e:
        raise RuntimeError("Error BioBERT model: {e}")
    
    diseases = [ent['word'] for ent in entities if ent['entity_group'] == 'DISEASE']
    drugs = [ent['word'] for ent in entities if ent['entity_group'] == 'DRUG']
    
    return diseases, drugs

# Compare the modals which is the best
def compareModal(x, y):
    commonRecord = set(x) & set(y)
    unique_x = set(x) - set(y)
    unique_y = set(y) - set(x)
    return commonRecord, unique_x, unique_y

# Main function to call all functions
def main():
    # please change the path according to your location
    filePath = r'E:\assgnement\group-assignment-python-code\outputtxt.txt'
    
    try:
        text = loadText(filePath)
    except (FileNotFoundError, IOError) as e:
        print(e)
        return
    
    # spacy models to get the disease
    try:
        diseaseSpacy, drugsSpacy = extractDisease(text, 'en_ner_bc5cdr_md')  #use anyone  or 'en_core_sci_sm'
    except RuntimeError as e:
        print(e)
        return
    
    # biobert model from the text
    try:
        diseasesBiobert, drugs_biobert = extractBiobert(text)
    except RuntimeError as e:
        print(e)
        return
    
    # Compare diseases from the text
    comDiseases, unidiseaseSpacy, uniDiseasesBiobert = compareModal(diseaseSpacy, diseasesBiobert)
    print(f"Common diseases: {comDiseases}")
    print(f"Unique diseases in SpaCy: {unidiseaseSpacy}")
    print(f"Unique diseases in BioBERT: {uniDiseasesBiobert}")
    
    # Compare drugs
    commDrugs, uniDrugsSpacy, uniDrugsBiobert = compareModal(drugsSpacy, drugs_biobert)
    print(f"Common drugs: {commDrugs}")
    print(f"Unique drugs (data) in SpaCy: {uniDrugsSpacy}")
    print(f"Unique drugs (Data) in BioBERT: {uniDrugsBiobert}")
    
    # Count most common entities in the text
    spEntitiesCount = Counter(diseaseSpacy + drugsSpacy)
    bioEntitiesCount = Counter(diseasesBiobert + drugs_biobert)
    
    print("Most common entities (data) in SpaCy:", spEntitiesCount.most_common(10))
    print("Most common entities (Data) in BioBERT:", bioEntitiesCount.most_common(10))

# Call all the above functions
if __name__ == "__main__":
    main()
