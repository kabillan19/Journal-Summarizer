from langchain_groq import ChatGroq
import streamlit as st

st.title("AI-Powered Daily Journal Summarizer")

prompt = st.text_input("Enter your prompt")

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=1,
    max_tokens=4096,  # Adjusted to the correct max tokens limit
    groq_api_key="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"
)

if st.button("Submit"):
    if prompt:
        response = llm.invoke("Generate a journal summary based on the following points: " + prompt)
        
        st.write("Response:\n")
        st.write(response.content)
    else:
        st.warning("Please enter a prompt.")
