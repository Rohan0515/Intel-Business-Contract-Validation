import spacy

def nlp_model(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    clauses = []
    clause_labels = [
        "agreement", "confidentiality", "party", "termination", "liability",
        "governing law", "jurisdiction", "indemnity", "warranty", "obligation",
        "payment", "force majeure", "amendment", "assignment", "severability",
        "dispute resolution", "arbitration", "intellectual property",
        "limitation of liability", "entire agreement"
    ]
    for sent in doc.sents:
        label = next((label for label in clause_labels if label in sent.text.lower()), "other")
        clauses.append({"text": sent.text.strip(), "label": label})
    return clauses

if __name__ == "__main__":
    content = "This agreement is made between the first party and the second party. The payment will be made in installments. Each party has certain obligations under this contract."
    classified_clauses = nlp_model(content)
    print("Classified Clauses:", classified_clauses)
