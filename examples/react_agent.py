# Example: ReAct (Reason + Act) Agent

# This script demonstrates the ReAct prompting technique, where the model reasons and takes actions (e.g., using a tool or API) in a loop.

import openai
openai.api_key = "YOUR_API_KEY"

def react_prompt(question):
    prompt = '''You are an agent that can reason and act. Answer the question step by step, and if you need to use a tool, say "Action: <tool> <input>". Otherwise, say "Final Answer: <answer>".

Question: What is the capital of France?
Thought: I need to recall the capital of France.
Final Answer: Paris

Question: What is 5 multiplied by 7?
Thought: I need to calculate 5 * 7.
Final Answer: 35

Question: {question}
Thought:'''.format(question=question)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    user_question = "Who wrote 'Pride and Prejudice'?"
    print("ReAct Output:")
    print(react_prompt(user_question))
