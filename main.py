from langchain_groq import ChatGroq
import streamlit as st

st.title("AI-Powered Daily Journal Summarizer")

prompt = st.text_input("Enter your prompt")

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=1,
<<<<<<< HEAD
    max_tokens=4096,  # Adjusted to the correct max tokens limit
    groq_api_key="API_KEY"
=======
    max_tokens=4096,  
    groq_api_key="API-KEY"
>>>>>>> a3a7229eea9a36bac82349d015cc849e8088e760
)

if st.button("Submit"):
    if prompt:
        response = llm.invoke(prompt)
        
        st.write("Response:\n")
        st.write(response.content)
    else:
        st.warning("Please enter a prompt.")
