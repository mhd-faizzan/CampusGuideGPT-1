import requests
import streamlit as st

def query_groq_llm(user_input):
    """Query the Groq LLM for responses."""
    api_key = st.secrets["GROQ_API_KEY"]  # Load API key from Streamlit secrets
    url = "https://api.groq.com/v1/chat/completions"  # Corrected API endpoint

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gemma-2b-it",  # Ensure this model is available in your Groq account
        "messages": [
            {"role": "system", "content": "You are an AI assistant providing information about universities."},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7,
        "max_tokens": 300
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Handle HTTP errors
        response_json = response.json()
        
        # Extract AI response
        return response_json.get("choices", [{}])[0].get("message", {}).get("content", "No response from AI.").strip()

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
