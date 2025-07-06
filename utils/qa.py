from openai import OpenAI
import os

# API anahtarını buradan al
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_question(context, question):
    response = client.chat.completions.create(
        model="gpt-4.1",  # Veya "gpt-4", "gpt-4-turbo" (Erişimin varsa)
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
        ]
    )
    return response.choices[0].message.content
