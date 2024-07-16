import json
from models.ocr_model.ocr_model import ocr_model
from models.nlp_model.nlp_model import nlp_model
from models.classification_model.classification_model import classification_model

def run_inference(contract_file, template_file):
    with open(contract_file, 'rb') as f:
        content = ocr_model(Image.open(f))
    
    parsed_content = nlp_model(content)
    
    with open(template_file, 'r') as f:
        template = json.load(f)
    
    deviations = classification_model(parsed_content, template["structure"])
    
    return deviations

if __name__ == "__main__":
    contract_file = "data/contracts/sample_contracts/contract1.pdf"
    template_file = "data/templates/template1.json"
    deviations = run_inference(contract_file, template_file)
    print("Deviations:", deviations)
