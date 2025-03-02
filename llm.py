import requests
import streamlit as st

def query_groq_llm(user_input):
    """Query the Groq LLM and return the AI response."""
    api_key = st.secrets["GROQ_API_KEY"]  # Load API key from Streamlit secrets
    url = "https://api.groq.com/openai/v1/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "gemma2-9b-it",
        "prompt": user_input,
        "max_tokens": 100
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Handle HTTP errors
        
        return response.json().get('choices', [{}])[0].get('text', 'No response from AI.').strip()

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
