import streamlit as st
import logging
import base64
from pathlib import Path
from openai import OpenAI, OpenAIError

# Configure logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration Constants
MODEL_NAME = "krikri-dpo-context"

def query_llm(prompt: str, api_key: str, api_endpoint: str) -> str:
    """
    Executes a request to the Krikri API using the OpenAI client library.
    """
    if not api_key:
        return "Error: API Key is missing. Please configure the application."
    
    if not api_endpoint:
        return "Error: API Endpoint is missing."

    try:
        # Initialize the client with the custom endpoint
        client = OpenAI(
            api_key=api_key,
            base_url=api_endpoint
        )

        logger.info(f"Sending request to {api_endpoint} using model {MODEL_NAME}")
        
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7, 
            max_tokens=500
        )

        return response.choices[0].message.content

    except OpenAIError as e:
        logger.error(f"OpenAI API Error: {e}")
        return f"API Error: {str(e)}"
    except Exception as e:
        logger.error(f"General Error: {e}")
        return f"An unexpected error occurred: {str(e)}"

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
        
        with st.spinner(f"Consulting {MODEL_NAME}..."):
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
    # Set the browser tab title
    st.set_page_config(
        page_title="PML 2025 students and the Krikri LLM", 
        layout="wide"
    )
    
    # Define available projects
    project_modules = {
        "Concept Explainer": project_concept_explainer,
        "The Excuse Generator": project_excuse_generator,
        "Hip-Hop Lyricist": project_lyricist,
        "Emoji Encoder": project_emoji_encoder
    }

    # Retrieve Secrets
    default_key = ""
    default_endpoint = ""
    credentials_loaded = False
    
    if "LLM_CREDENTIALS" in st.secrets:
        try:
            default_key = st.secrets["LLM_CREDENTIALS"]["API_KEY"]
            default_endpoint = st.secrets["LLM_CREDENTIALS"]["API_ENDPOINT"]
            credentials_loaded = True
        except KeyError:
            logger.warning("Secrets found but keys are missing.")

    with st.sidebar:
        # --- BRANDING SECTION ---
        st.title("PML 2025 students using an LLM named")
        
        logo_path = Path("logo.jpg")
        target_url = "https://chat.ilsp.gr"

        if logo_path.exists():
            try:
                with open(logo_path, "rb") as f:
                    img_bytes = f.read()
                encoded = base64.b64encode(img_bytes).decode()
                
                # Clickable Logo
                html_code = f'''
                    <a href="{target_url}" target="_blank">
                        <img src="data:image/jpeg;base64,{encoded}" width="150" style="margin-top: 10px; margin-bottom: 10px;">
                    </a>
                '''
                st.markdown(html_code, unsafe_allow_html=True)
            except Exception as e:
                logger.error(f"Failed to process logo image: {e}")
        
        # URL Link below the logo
        st.markdown(f"[{target_url}]({target_url})")

        st.divider()
        
        # --- APP SELECTOR ---
        st.subheader("Select App")
        selection = st.radio("Available Tools:", list(project_modules.keys()))
        
        st.divider()
        
        # --- CONFIGURATION (Expandable) ---
        with st.expander("Configuration", expanded=not credentials_loaded):
            if credentials_loaded:
                st.success("Credentials loaded from Secrets.")
            else:
                st.info("Running in manual mode.")

            api_key_display = st.text_input(
                "LLM API Key", 
                value=default_key, 
                type="password",
                disabled=credentials_loaded,
                help="Loaded from st.secrets" if credentials_loaded else "Enter key"
            )
            
            endpoint_display = st.text_input(
                "LLM Endpoint URL", 
                value=default_endpoint,
                disabled=credentials_loaded,
                help="Loaded from st.secrets" if credentials_loaded else "Enter endpoint"
            )
    
    # Execute Selected Project
    if selection in project_modules:
        try:
            project_modules[selection](api_key_display, endpoint_display)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
