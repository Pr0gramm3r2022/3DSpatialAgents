import os
import streamlit as st
from google import genai
from google.genai.errors import APIError 

# ... (other imports) ...

@st.cache_resource(show_spinner=False)
def get_client() -> genai.Client:
    """
    Initializes and returns the Gemini API client.
    Prioritizes reading the API key from environment variables or st.secrets.
    """
    api_key = None
    
    # Check for the key directly in the operating system environment
    if "GEMINI_API_KEY" in os.environ:
        api_key = os.environ[".env"]
        st.success("API Key loaded from OS environment.")
        
    # Fallback: Check Streamlit secrets, which is necessary for Streamlit Cloud
    elif "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets[""]
        st.success("API Key loaded from Streamlit secrets.")
    
    # Final check and error handling
    if not api_key:
        st.error(
            "🚨 **API Key not found.** Please set the `GEMINI_API_KEY` "
            "as a Codespaces Secret, an environment variable, or in your `secrets.toml` file."
        )
        st.stop()
        
    # The client initializes itself using the api_key parameter
    # The google-genai library can also often find the key if it's just set 
    # as an environment variable, but explicitly passing it is the most reliable.
    return genai.Client(api_key=api_key) 

# ... (rest of the code) ...
