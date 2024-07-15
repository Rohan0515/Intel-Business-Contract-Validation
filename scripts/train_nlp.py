import spacy

def train_nlp_model(training_data_dir):
    nlp = spacy.load("en_core_web_sm")
    nlp.to_disk("models/nlp_model/")

if __name__ == "__main__":
    train_nlp_model("data/preprocessed")
