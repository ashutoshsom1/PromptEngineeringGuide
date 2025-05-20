# Example: Few-shot Prompting

# This Python script demonstrates few-shot prompting for sentiment analysis.


import openai

openai.api_key = "YOUR_API_KEY"

prompt = """
Classify the sentiment of the following sentences as Positive, Negative, or Neutral.

Sentence: I love this product!
Sentiment: Positive

Sentence: This is terrible.
Sentiment: Negative

Sentence: It's okay, nothing special.
Sentiment: Neutral

Sentence: I'm so happy with my purchase!
Sentiment:
"""

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=10
)

print(response.choices[0].text.strip())


# Replace `YOUR_API_KEY` with your actual OpenAI API key.
