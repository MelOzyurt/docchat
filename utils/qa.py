from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])  # Veya direkt openai_key = "..."

def ask_question(context, question):
    response = client.chat.completions.create(
        model="gpt-4o",  # "gpt-4o" da olabilir
        messages=[
            {"role": "system", "content": "You answer questions based only on the uploaded content."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
        ]
    )
    return response.choices[0].message.content.strip()
