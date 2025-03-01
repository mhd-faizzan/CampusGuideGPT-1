import requests
import streamlit as st
from backend import get_university_info

# Load API key from Streamlit secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_MODEL = "gemma-2b-it"

def query_groq_llm(query):
    retrieved_info = get_university_info(query)
    
    structured_data = "\n".join([f"{col}: {retrieved_info[col]}" for col in retrieved_info.index])

    prompt = f"Here is relevant information from Hochschule Harz database:\n{structured_data}\nNow answer this query: {query}"

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5,
        "max_tokens": 300
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json().get("choices", [{}])[0].get("message", {}).get("content", "").strip()
