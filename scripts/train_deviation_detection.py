import json
import os

def train_deviation_detection_model(template_file, training_data_dir):
    with open(template_file, 'r') as f:
        template = json.load(f)

    deviations = []
    for filename in os.listdir(training_data_dir):
        if filename.endswith(".json"):
            with open(os.path.join(training_data_dir, filename), 'r') as f:
                data = json.load(f)
                for item in data:
                    if item["label"] in template["structure"] and item["text"] not in template["structure"][item["label"]]:
                        deviations.append(item)
    with open("models/deviation_detection_model/model.json", 'w') as f:
        json.dump(deviations, f)

if __name__ == "__main__":
    train_deviation_detection_model("data/templates/template1.json", "data/preprocessed")
