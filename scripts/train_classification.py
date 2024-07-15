import os
import json

def train_classification_model(training_data_dir):
    model = {}
    for filename in os.listdir(training_data_dir):
        if filename.endswith(".json"):
            with open(os.path.join(training_data_dir, filename), 'r') as f:
                data = json.load(f)
                for item in data:
                    label = classify_clause(item["text"])
                    if label not in model:
                        model[label] = []
                    model[label].append(item["text"])
    with open("models/classification_model/model.json", 'w') as f:
        json.dump(model, f)

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
    train_classification_model("data/preprocessed")
