import openai
import os

def ask_question(context, question):
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions about a document."},
            {"role": "user", "content": f"Document: {context}"},
            {"role": "user", "content": f"Question: {question}"}
        ]
    )

    return response.choices[0].message.content.strip()
