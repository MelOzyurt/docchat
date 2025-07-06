import streamlit as st
from utils.extract import *
from utils.qa import ask_question

st.set_page_config(page_title="📄 Chat with Your Document")

st.title("📄 Chat with Your Document")
st.markdown("Upload a document and ask questions about its content.")

# Initialize state
chat_history = st.session_state.setdefault("chat_history", [])
context = st.session_state.setdefault("doc_text", "")

# File upload
uploaded_file = st.file_uploader(
    "Upload file (PDF, DOCX, CSV, XLSX)", type=["pdf", "docx", "csv", "xls", "xlsx"]
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
    st.session_state.doc_text = context[:100000]  # truncate to avoid token limits

# Display all previous messages
for sender, msg in chat_history:
    with st.chat_message("user" if sender == "You" else "ai"):
        st.markdown(msg)

# Chat input at bottom, using chat_input (ENTER key submits automatically)
if context:
    user_input = st.chat_input("Ask something about the document...")

    if user_input:
        # Add user's message to history
        st.session_state.chat_history.append(("You", user_input))

        # Generate AI answer
        answer = ask_question(context, user_input)

        # Add AI's response to history
        st.session_state.chat_history.append(("AI", answer))

        # Re-run to show latest chat messages
        st.rerun()
else:
    st.info("Please upload a document first.")
