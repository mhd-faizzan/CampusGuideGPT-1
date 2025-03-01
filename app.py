import streamlit as st
from llm import query_groq_llm
from backend import get_university_info

st.title("CampusGuideGPT - Hochschule Harz")

user_input = st.text_input("Ask me anything about Hochschule Harz:")

if user_input:
    structured_data = get_university_info(user_input)
    
    if structured_data is not None:
        st.write("### Retrieved University Info:")
        st.write(structured_data.to_dict())

    llm_response = query_groq_llm(user_input)
    st.write("### AI Response:")
    st.write(llm_response)