# Example: Chain-of-Thought Prompting

# This Python script demonstrates chain-of-thought prompting for arithmetic reasoning.

# ```python
import openai

openai.api_key = "YOUR_API_KEY"

prompt = """
Q: If there are 3 cars and each car has 4 wheels, how many wheels are there in total?
A: There are 3 cars. Each car has 4 wheels. So, 3 x 4 = 12 wheels in total.

Q: If there are 5 boxes and each box contains 8 apples, how many apples are there in total?
A:
"""

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=50
)

print(response.choices[0].text.strip())
# ```

# Replace `YOUR_API_KEY` with your actual OpenAI API key.
