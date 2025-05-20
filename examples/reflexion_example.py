# Example: Reflexion Technique

# This script demonstrates the Reflexion prompting technique, where the model reflects on its previous answer and iteratively improves it.

import openai
openai.api_key = "YOUR_API_KEY"

def reflexion_prompt(question, initial_answer):
    prompt = f"""Question: {question}
Initial Answer: {initial_answer}
Reflect on the answer above. If it is incorrect or incomplete, provide an improved answer. Otherwise, confirm it is correct.
Reflection:"""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    question = "What is the capital of Australia?"
    initial_answer = "Sydney"
    print("Reflexion Output:")
    print(reflexion_prompt(question, initial_answer))
