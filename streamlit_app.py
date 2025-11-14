import streamlit as st
import logging

# Configure logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def query_llm(prompt: str, api_key: str, api_endpoint: str) -> str:
    """
    Centralized function to handle remote LLM API calls.
    """
    if not api_key:
        return "Error: API Key is missing."
    
    try:
        # Simulation return
        # In production: response = requests.post(api_endpoint, headers=..., json=...)
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

def render_configuration_gate():
    """
    Renders the initial setup form.
    This is only shown if credentials are missing from session state.
    """
    st.title("PML 2025 Students")
    st.subheader("System Configuration")
    st.info("Please enter the provided LLM credentials to access the laboratory tools.")
    
    with st.form("config_form"):
        key_input = st.text_input("API Key", type="password")
        endpoint_input = st.text_input("Endpoint URL")
        
        submitted = st.form_submit_button("Initialize System")
        
        if submitted:
            if key_input and endpoint_input:
                st.session_state["api_key"] = key_input
                st.session_state["api_endpoint"] = endpoint_input
                st.success("Configuration saved. Loading tools...")
                st.rerun()
            else:
                st.error("Both API Key and Endpoint are required.")

def main():
    st.set_page_config(page_title="PML 2025 Students", layout="wide")
    
    # Initialize Session State logic
    if "api_key" not in st.session_state:
        st.session_state["api_key"] = None
    if "api_endpoint" not in st.session_state:
        st.session_state["api_endpoint"] = None

    # Check if we are authenticated (Gate Logic)
    if not st.session_state["api_key"]:
        render_configuration_gate()
        return # Stop execution here until configured

    # --- Main Application Logic (Only reachable after configuration) ---
    
    with st.sidebar:
        st.title("PML 2025 students")
        st.divider()
        
        st.subheader("Navigation")
        
        # Project Dispatcher
        project_modules = {
            "Concept Explainer": project_concept_explainer,
            "The Excuse Generator": project_excuse_generator,
            "Hip-Hop Lyricist": project_lyricist,
            "Emoji Encoder": project_emoji_encoder
        }
        
        selection = st.sidebar.radio("Select Tool:", list(project_modules.keys()))
        
        st.divider()
        
        # Reset Button (In case they entered the wrong key)
        if st.button("Reset Configuration"):
            st.session_state["api_key"] = None
            st.session_state["api_endpoint"] = None
            st.rerun()
    
    # Execute Selected Project
    if selection in project_modules:
        current_function = project_modules[selection]
        try:
            # Pass the credentials from session state
            current_function(
                st.session_state["api_key"], 
                st.session_state["api_endpoint"]
            )
        except Exception as e:
            st.error(f"An error occurred: {e}")
            logger.error(f"Module error: {e}")

if __name__ == "__main__":
    main()
