# Example: Zero-shot Prompting

# This Python script demonstrates zero-shot prompting using the OpenAI API.

import openai

openai.api_key = "YOUR_API_KEY"

prompt = "Translate the following English text to French: 'How are you today?'"

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=60
)

print(response.choices[0].text.strip())

# Replace `YOUR_API_KEY` with your actual OpenAI API key.
