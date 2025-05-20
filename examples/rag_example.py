# Example: Retrieval Augmented Generation (RAG)

# This script demonstrates a simple RAG workflow, where the model is provided with retrieved context to answer a question.

import openai
openai.api_key = "YOUR_API_KEY"

def rag_prompt(context, question):
    prompt = f"""Use the following context to answer the question.

Context: {context}

Question: {question}
Answer:"""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    context = "Jane Austen was an English novelist known primarily for her six major novels, including 'Pride and Prejudice'."
    question = "Who wrote 'Pride and Prejudice'?"
    print("RAG Output:")
    print(rag_prompt(context, question))
