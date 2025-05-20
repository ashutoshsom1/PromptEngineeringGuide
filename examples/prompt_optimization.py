# Example: Prompt Optimization

# This script demonstrates how prompt clarity and specificity can improve LLM output.

# Before: Vague prompt
vague_prompt = "Summarize this."

# After: Clear, specific prompt
clear_prompt = "Summarize the following article in three bullet points: Artificial intelligence is transforming industries by automating tasks, improving decision-making, and enabling new products and services."

import openai
openai.api_key = "YOUR_API_KEY"

print("--- Vague Prompt Output ---")
vague_response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=vague_prompt + "\nArticle: Artificial intelligence is transforming industries by automating tasks, improving decision-making, and enabling new products and services.",
    max_tokens=60
)
print(vague_response.choices[0].text.strip())

print("\n--- Clear Prompt Output ---")
clear_response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=clear_prompt,
    max_tokens=60
)
print(clear_response.choices[0].text.strip())
