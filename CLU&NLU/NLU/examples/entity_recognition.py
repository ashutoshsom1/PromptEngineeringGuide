# NLU Example: Named Entity Recognition (NER) with spaCy

# This script demonstrates how to use spaCy for entity recognition in text.

import spacy

# Load the English NLP model
nlp = spacy.load('en_core_web_sm')

text = "Apple is looking at buying U.K. startup for $1 billion."
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)


# You can install spaCy and the model with:
# powershell
# pip install spacy
# python -m spacy download en_core_web_sm

