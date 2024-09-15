import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
from collections import Counter

# function to read the txt file
def loadText(filePath):
    with open(filePath, 'r') as file:
        return file.read()

# Extract model
def extractDisease(text, modelName):
    #load the modal name
    nlp = spacy.load(modelName)
    doc = nlp(text)
    diseases = [ent.text for ent in doc.ents if ent.label_ == 'DISEASE']
    drugs = [ent.text for ent in doc.ents if ent.label_ == 'DRUG']
    return diseases, drugs

# function biobert model
def extractBiobert(text):
    tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
    model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
    nlp = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")
    entities = nlp(text)
    diseases = [ent['word'] for ent in entities if ent['entity_group'] == 'DISEASE']
    drugs = [ent['word'] for ent in entities if ent['entity_group'] == 'DRUG']
    return diseases, drugs

# Compare the modals which is the best
def compareModal(x, y):
    commonRecord = set(x) & set(y)
    unique_x = set(x) - set(y)
    unique_y = set(y) - set(x)
    return commonRecord, unique_x, unique_y

# Main function to call the all function
def main():
    text = loadText(r'E:\assgnement\group-assignment-python-code\outputtxt.txt')
    
    # spacy models to get the desiese
    diseaseSpacy, drugsSpacy = extractDisease(text, 'en_ner_bc5cdr_md')  #use anyone  or 'en_core_sci_sm'
    
    # biobert model from tha Txt
    diseasesBiobert, drugs_biobert = extractBiobert(text)
    
    # Compare diseases from tha Txt
    comDiseases, unidiseaseSpacy, uniDiseasesBiobert = compareModal(diseaseSpacy, diseasesBiobert)
    print(f"Common diseases: {comDiseases}")
    print(f"Unique diseases in SpaCy: {unidiseaseSpacy}")
    print(f"Unique diseases in BioBERT: {uniDiseasesBiobert}")
    
    # Compare drugs
    commDrugs, uniDrugsSpacy, uniDrugsBiobert = compareModal(drugsSpacy, drugs_biobert)
    print(f"Common drugs: {commDrugs}")
    print(f"Unique drugs(data) in SpaCy: {uniDrugsSpacy}")
    print(f"Unique drugs(Data) in BioBERT: {uniDrugsBiobert}")
    
    # Count most common entities in the txt
    spEntitiesCount = Counter(diseaseSpacy + drugsSpacy)
    bioEntitiesCount = Counter(diseasesBiobert + drugs_biobert)
    
    print("Most common entities(data) in SpaCy:", spEntitiesCount.most_common(10))
    print("Most common entities(Data) in BioBERT:", bioEntitiesCount.most_common(10))
# calll the al above data
if __name__ == "__main__":
    main()
