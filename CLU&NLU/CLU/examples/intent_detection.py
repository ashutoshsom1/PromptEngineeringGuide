# CLU Example: Intent Detection with Hugging Face Transformers

# This script demonstrates how to use a pre-trained transformer model for intent classification in conversational text.

from transformers import pipeline

# Load a zero-shot classification pipeline
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

candidate_labels = ['book_flight', 'check_weather', 'play_music', 'order_food']
text = "I want to book a flight to Paris next week."

result = classifier(text, candidate_labels)
print("Intent:", result['labels'][0])


# This approach can be adapted for custom intent sets and fine-tuned models.
