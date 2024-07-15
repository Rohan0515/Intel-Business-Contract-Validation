import spacy

nlp = spacy.load("en_core_web_sm")

def classify_clauses(content):
    doc = nlp(content)
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
        clauses.append({"text": sent.text, "label": label})
    return clauses
