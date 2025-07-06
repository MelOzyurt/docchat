import streamlit as st
from utils.extract import *
from utils.qa import ask_question

st.set_page_config(page_title="📄 Chat with Your Document")

st.title("📄 Chat with Your Document")
st.markdown("Upload a document and ask questions about its content.")

# Initialize session state for chat history and context
chat_history = st.session_state.setdefault("chat_history", [])
context = st.session_state.setdefault("doc_text", "")

# File uploader
uploaded_file = st.file_uploader(
    "Upload file (PDF, DOCX, CSV, XLSX)",
    type=["pdf", "docx", "csv", "xls", "xlsx"]
)

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1].lower()
    if file_type == "pdf":
        context = extract_text_from_pdf(uploaded_file)
    elif file_type == "docx":
        context = extract_text_from_docx(uploaded_file)
    elif file_type == "csv":
        context = extract_text_from_csv(uploaded_file)
    elif file_type in ["xls", "xlsx"]:
        context = extract_text_from_excel(uploaded_file)
    else:
        st.error("Unsupported file type.")
    # Save truncated context for token limits
    st.session_state.doc_text = context[:100000]

# Display chat messages
for sender, msg in chat_history:
    st.chat_message(sender.lower()).write(msg)

# Input form at bottom
with st.form(key="chat_form", clear_on_submit=True):
    question = st.text_input("Ask a question:")
    send = st.form_submit_button("Send")

if send and question and context:
    answer = ask_question(context, question)
    chat_history.append(("You", question))
    chat_history.append(("AI", answer))
    st.experimental_rerun()
elif send and not context:
    st.warning("Please upload a document first.")
