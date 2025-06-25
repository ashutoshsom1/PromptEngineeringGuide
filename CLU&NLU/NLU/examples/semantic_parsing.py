# NLU Example: Semantic Parsing with Hugging Face Transformers

# This script demonstrates a simple approach to semantic parsing using a text-to-text transformer model.

from transformers import pipeline

# Load a text2text-generation pipeline (e.g., T5)
parser = pipeline('text2text-generation', model='t5-small')

text = "Convert to SQL: Show me all flights from Paris to Berlin on June 10th."
result = parser(text, max_length=64)
print("Semantic Parse:", result[0]['generated_text'])


# This approach can be adapted for more complex parsing tasks and fine-tuned models.
