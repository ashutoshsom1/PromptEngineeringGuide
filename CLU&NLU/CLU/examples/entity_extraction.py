# CLU Example: Entity Extraction with Hugging Face Transformers

# This script demonstrates how to use a pre-trained transformer model for entity extraction (NER) in conversational text.


from transformers import pipeline

# Load a named entity recognition pipeline
ner = pipeline('ner', grouped_entities=True)

text = "Book a flight from New York to Paris on June 10th."

entities = ner(text)
print("Entities:", entities)


# This approach can be adapted for slot filling and custom entity types.
