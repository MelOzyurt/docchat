import openai
import streamlit as st

# OpenAI API key is securely read from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

def ask_question(context, question):
    response = openai.ChatCompletion.create(
        model="gpt-4.0",
        messages=[
            {"role": "system", "content": "You answer questions based only on the uploaded content."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
        ]
    )
    return response.choices[0].message.content.strip()
