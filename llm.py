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
    
    # Improving the prompt for better AI responses
    prompt = f"You are an AI assistant helping students find university programs. Provide additional insights about this query:\n\n{user_input}"

    data = {
        "model": "gemma2-9b-it",
        "prompt": prompt,
        "max_tokens": 200,
        "temperature": 0.7  # Making the response more creative
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Handle HTTP errors

        # Print the response for debugging
        response_json = response.json()
        print("Groq API Response:", response_json)  # Debugging output
        
        return response_json.get('choices', [{}])[0].get('text', 'No response from AI.').strip()

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
