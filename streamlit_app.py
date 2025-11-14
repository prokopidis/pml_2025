import streamlit as st
import logging
import requests
import json
import os
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration Constants
# Replace this URL with the raw URL where you pasted the ENCRYPTED_CONTENT
CONFIG_URL = "[https://gist.githubusercontent.com/user/id/raw/encrypted_config.txt](https://gist.githubusercontent.com/user/id/raw/encrypted_config.txt)"

def load_secure_config(decryption_key: str) -> dict:
    """
    Fetches encrypted config from the web and decrypts it.
    """
    try:
        # Fetch the encrypted payload
        response = requests.get(CONFIG_URL, timeout=10)
        response.raise_for_status()
        encrypted_content = response.content

        # Decrypt the payload
        cipher_suite = Fernet(decryption_key)
        decrypted_json = cipher_suite.decrypt(encrypted_content).decode('utf-8')
        
        logger.info("Secure configuration loaded and decrypted successfully.")
        return json.loads(decrypted_json)
        
    except Exception as e:
        logger.error(f"Failed to load secure config: {e}")
        return {}

def query_llm(prompt: str, api_key: str, api_endpoint: str) -> str:
    """
    Centralized function to handle remote LLM API calls.
    """
    if not api_key:
        return "Error: API Key is missing. Please configure the application."
    
    try:
        # Simulation return
        logger.info(f"Sending request to {api_endpoint}")
        return f"Simulated LLM Output from {api_endpoint} for: {prompt}"
    except Exception as e:
        logger.error(f"API Call failed: {e}")
        return "Error: Could not retrieve response from LLM."

def project_concept_explainer(api_key: str, api_endpoint: str):
    """
    Complete Implementation: Concept Explainer.
    """
    st.header("Concept Explainer")
    st.write("Enter a complex topic and select an audience.")

    topic_input = st.text_area("Enter the concept to explain", height=100)
    complexity_level = st.selectbox(
        "Target Audience",
        ["Five-year-old", "High School Student", "University Professor"]
    )

    if st.button("Generate Explanation"):
        if not topic_input:
            st.warning("Please enter a topic first.")
            return
        
        final_prompt = (
            f"Explain the concept of '{topic_input}' "
            f"specifically to a {complexity_level}."
        )
        
        with st.spinner("Consulting the LLM..."):
            result = query_llm(final_prompt, api_key, api_endpoint)
            
        st.subheader("Result")
        st.markdown(result)

def project_excuse_generator(api_key: str, api_endpoint: str):
    """
    Stub: The Excuse Generator.
    """
    st.header("The Excuse Generator")
    st.write("Generate a creative reason for a social infraction.")
    
    situation = st.text_input("What did you mess up? (e.g., 'Forgot homework')")
    intensity = st.slider("Craziness Level", 1, 10, 5)
    
    if st.button("Make an Excuse"):
        st.info("Student implementation required here.")

def project_lyricist(api_key: str, api_endpoint: str):
    """
    Stub: Hip-Hop Lyricist.
    """
    st.header("Hip-Hop Lyricist")
    st.write("Drop a beat and a topic.")
    
    topic = st.text_input("Topic (e.g., 'Quantum Physics', 'School Lunch')")
    style = st.selectbox("Style", ["Old School", "Trap", "Mumble Rap"])
    
    if st.button("Drop Verses"):
        st.info("Student implementation required here.")

def project_emoji_encoder(api_key: str, api_endpoint: str):
    """
    Stub: Emoji Encoder.
    """
    st.header("Emoji Encoder")
    st.write("Translate your text entirely into emojis.")
    
    user_text = st.text_area("Enter message to encode")
    
    if st.button("Encode"):
        st.info("Student implementation required here.")

def main():
    st.set_page_config(page_title="PML 2025 Students", layout="wide")
    
    # Initialize session state for credentials if not present
    if "api_key" not in st.session_state:
        st.session_state["api_key"] = ""
    if "api_endpoint" not in st.session_state:
        st.session_state["api_endpoint"] = ""
    
    with st.sidebar:
        # Branding Title Only
        st.title("PML 2025 students")
        st.divider()
        
        st.subheader("Configuration")

        # 1. Attempt to load from Environment Variable "MASTER_KEY"
        env_key = os.environ.get("MASTER_KEY")
        
        # 2. Manual Override if Env var is missing
        if not env_key:
            decryption_key = st.text_input("Enter Decryption Master Key", type="password")
        else:
            decryption_key = env_key
            st.success("Master Key loaded from environment.")

        # 3. Load Config Logic
        if decryption_key and not st.session_state["api_key"]:
            config = load_secure_config(decryption_key)
            if config:
                st.session_state["api_key"] = config.get("api_key", "")
                st.session_state["api_endpoint"] = config.get("api_endpoint", "")
                st.success("Credentials successfully decrypted and applied.")
            else:
                st.error("Decryption failed. Check Key or URL.")

        # 4. Display Fields (Disabled if loaded successfully, Editable if manual fallback needed)
        api_key_display = st.text_input(
            "LLM API Key", 
            value=st.session_state["api_key"], 
            type="password",
            disabled=bool(st.session_state["api_key"]) 
        )
        
        endpoint_display = st.text_input(
            "LLM Endpoint URL", 
            value=st.session_state["api_endpoint"],
            disabled=bool(st.session_state["api_endpoint"])
        )

        st.divider()
        st.subheader("Select App")
    
    # Update local variables to ensure they pass to functions
    final_key = api_key_display
    final_endpoint = endpoint_display

    project_modules = {
        "Concept Explainer": project_concept_explainer,
        "The Excuse Generator": project_excuse_generator,
        "Hip-Hop Lyricist": project_lyricist,
        "Emoji Encoder": project_emoji_encoder
    }
    
    selection = st.sidebar.radio("Available Tools:", list(project_modules.keys()))
    
    if selection in project_modules:
        try:
            project_modules[selection](final_key, final_endpoint)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
