import os
from PIL import Image
import pytesseract
import spacy
import json

def preprocess_contracts(contract_dir, output_dir):
    nlp = spacy.load("en_core_web_sm")
    for filename in os.listdir(contract_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(contract_dir, filename)
            image = Image.open(pdf_path)
            text = pytesseract.image_to_string(image)
            doc = nlp(text)
            preprocessed_text = [{"text": sent.text, "label": classify_clause(sent.text)} for sent in doc.sents]
            output_path = os.path.join(output_dir, filename.replace(".pdf", ".json"))
            with open(output_path, 'w') as f:
                json.dump(preprocessed_text, f)

def classify_clause(text):
    clause_labels = [
        "agreement", "confidentiality", "party", "termination", "liability",
        "governing law", "jurisdiction", "indemnity", "warranty", "obligation",
        "payment", "force majeure", "amendment", "assignment", "severability",
        "dispute resolution", "arbitration", "intellectual property",
        "limitation of liability", "entire agreement"
    ]
    label = next((label for label in clause_labels if label in text.lower()), "other")
    return label

if __name__ == "__main__":
    preprocess_contracts("data/contracts/sample_contracts", "data/preprocessed")
