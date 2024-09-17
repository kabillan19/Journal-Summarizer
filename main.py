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
        response = llm.invoke(prompt)
        
        st.write("Response:\n")
        st.write(response.content)
    else:
        st.warning("Please enter a prompt.")
