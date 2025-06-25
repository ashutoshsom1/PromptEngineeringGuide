# NLU Example: Text Classification with Hugging Face Transformers

# This script demonstrates how to use a pre-trained transformer model for text classification.


from transformers import pipeline

# Load a text classification pipeline
classifier = pipeline('text-classification', model='distilbert-base-uncased-finetuned-sst-2-english')

text = "The movie was fantastic!"
result = classifier(text)
print("Label:", result[0]['label'], "Score:", result[0]['score'])


# This approach can be adapted for custom classification tasks and fine-tuned models.
