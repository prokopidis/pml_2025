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
    Intended to generate creative excuses for specific scenarios.
    """
    st.header("The Excuse Generator")
    st.write("Generate a creative reason for a social infraction.")
    
    situation = st.text_input("What did you mess up? (e.g., 'Forgot homework')")
    intensity = st.slider("Craziness Level", 1, 10, 5)
    
    if st.button("Make an Excuse"):
        # logic: prompt = f"Write an excuse for {situation} that is {intensity}/10 crazy."
        st.info("Student implementation required here.")

def project_lyricist(api_key: str):
    """
    Stub: Hip-Hop Lyricist.
    Intended to write verses on a topic.
    """
    st.header("Hip-Hop Lyricist")
    st.write("Drop a beat and a topic.")
    
    topic = st.text_input("Topic (e.g., 'Quantum Physics', 'School Lunch')")
    style = st.selectbox("Style", ["Old School", "Trap", "Mumble Rap"])
    
    if st.button("Drop Verses"):
        # logic: prompt = f"Write 8 bars of {style} lyrics about {topic}."
        st.info("Student implementation required here.")

def project_emoji_encoder(api_key: str):
    """
    Stub: Emoji Encoder.
    Intended to translate text to emojis.
    """
    st.header("Emoji Encoder")
    st.write("Translate your text entirely into emojis.")
    
    user_text = st.text_area("Enter message to encode")
    
    if st.button("Encode"):
        # logic: prompt = f"Rewrite the following sentence using only emojis: {user_text}"
        st.info("Student implementation required here.")

def main():
    st.set_page_config(page_title="Student AI Labs", layout="wide")
    
    with st.sidebar:
        st.title("Configuration")
        api_key = st.text_input("Enter LLM API Key", type="password")
        st.divider()
        st.title("Select App")
    
    # Dictionary Dispatcher
    # Students can add new projects by adding a Key:Value pair here
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
