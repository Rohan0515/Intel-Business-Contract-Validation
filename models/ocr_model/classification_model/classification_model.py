import json

def classification_model(clauses, template):
    deviations = []
    for clause in clauses:
        label = clause['label']
        if label in template and clause['text'].lower() not in template[label]:
            deviations.append(clause)
    return deviations

if __name__ == "__main__":
    template = {
        "agreement": ["agreement"],
        "confidentiality": ["confidentiality"],
        "party": ["party"],
        "termination": ["termination"],
        "liability": ["liability"],
        "governing law": ["governing law"],
        "jurisdiction": ["jurisdiction"],
        "indemnity": ["indemnity"],
        "warranty": ["warranty"],
        "obligation": ["obligation"],
        "payment": ["payment"],
        "force majeure": ["force majeure"],
        "amendment": ["amendment"],
        "assignment": ["assignment"],
        "severability": ["severability"],
        "dispute resolution": ["dispute resolution"],
        "arbitration": ["arbitration"],
        "intellectual property": ["intellectual property"],
        "limitation of liability": ["limitation of liability"],
        "entire agreement": ["entire agreement"]
    }
    parsed_clauses = [
        {"text": "This agreement is made between the first party and the second party.", "label": "party"},
        {"text": "The payment will be made in installments.", "label": "payment"},
        {"text": "Each party has certain obligations under this contract.", "label": "obligation"},
        {"text": "Unauthorized clause", "label": "other"}
    ]
    deviations = classification_model(parsed_clauses, template)
    print("Deviations:", deviations)
