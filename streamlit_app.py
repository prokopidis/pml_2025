import streamlit as st
import logging

# Configure logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def query_llm(prompt: str, api_key: str) -> str:
    """
    Centralized function to handle remote LLM API calls.
    """
    if not api_key:
        raise ValueError("API Key is missing")
    
    try:
        # Simulation return for demonstration
        logger.info(f"Mock LLM call executed for prompt: {prompt[:30]}...")
        return f"Simulated LLM Output for: {prompt}"
        
    except Exception as e:
        logger.error(f"API Call failed: {e}")
        return "Error: Could not retrieve response from LLM."

def project_concept_explainer(api_key: str):
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
            result = query_llm(final_prompt, api_key)
            
        st.subheader("Result")
        st.markdown(result)

def project_excuse_generator(api_key: str):
    """
    Stub: The Excuse Generator.
    """
    st.header("The Excuse Generator")
    st.write("Generate a creative reason for a social infraction.")
    
    situation = st.text_input("What did you mess up? (e.g., 'Forgot homework')")
    intensity = st.slider("Craziness Level", 1, 10, 5)
    
    if st.button("Make an Excuse"):
        # prompt logic goes here
        st.info("Student implementation required here.")

def project_lyricist(api_key: str):
    """
    Stub: Hip-Hop Lyricist.
    """
    st.header("Hip-Hop Lyricist")
    st.write("Drop a beat and a topic.")
    
    topic = st.text_input("Topic (e.g., 'Quantum Physics', 'School Lunch')")
    style = st.selectbox("Style", ["Old School", "Trap", "Mumble Rap"])
    
    if st.button("Drop Verses"):
        # prompt logic goes here
        st.info("Student implementation required here.")

def project_emoji_encoder(api_key: str):
    """
    Stub: Emoji Encoder.
    """
    st.header("Emoji Encoder")
    st.write("Translate your text entirely into emojis.")
    
    user_text = st.text_area("Enter message to encode")
    
    if st.button("Encode"):
        # prompt logic goes here
        st.info("Student implementation required here.")

def main():
    st.set_page_config(page_title="PML 2025 Students", layout="wide")
    
    with st.sidebar:
        # Branding Section
        try:
            st.image(
                "[https://siteresources.blob.core.windows.net/siteresourcescontainer/hauportal/media/root/settings/header/hellenic-american-union.svg](https://siteresources.blob.core.windows.net/siteresourcescontainer/hauportal/media/root/settings/header/hellenic-american-union.svg)", 
                use_container_width=True
            )
        except Exception as e:
            logger.error(f"Image load failed: {e}")
            st.write("Hellenic American Union")
            
        st.title("PML 2025 students")
        st.divider()
        
        # Configuration Section
        st.subheader("Configuration")
        api_key = st.text_input("Enter LLM API Key", type="password")
        st.divider()
        st.subheader("Select App")
    
    # Dictionary Dispatcher
    project_modules = {
        "Concept Explainer": project_concept_explainer,
        "The Excuse Generator": project_excuse_generator,
        "Hip-Hop Lyricist": project_lyricist,
        "Emoji Encoder": project_emoji_encoder
    }
    
    selection = st.sidebar.radio("Available Tools:", list(project_modules.keys()))
    
    if selection in project_modules:
        current_function = project_modules[selection]
        try:
            current_function(api_key)
        except Exception as e:
            st.error(f"An error occurred in the module: {e}")
            logger.error(f"Module execution error: {e}")

if __name__ == "__main__":
    main()
