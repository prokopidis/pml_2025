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

    # Main Input
    topic_input = st.text_area("Enter the concept to explain", height=100)
    
    # Configuration Options (Vertical Layout)
    complexity_level = st.selectbox(
        "Target Audience",
        ["Five-year-old", "High School Student", "University Professor"]
    )
    
    output_language = st.radio(
        "Output Language",
        ["English", "Greek"],
        horizontal=True 
    )

    if st.button("Generate Explanation"):
        if not topic_input:
            st.warning("Please enter a topic first.")
            return
        
        # Updated Prompt with Language Instruction
        final_prompt = (
            f"Explain the concept of '{topic_input}' "
            f"specifically to a {complexity_level}. "
            f"Provide the explanation in {output_language}."
        )
        
        with st.spinner(f"Consulting {MODEL_NAME}..."):
            result = query_llm(final_prompt, api_key, api_endpoint)
            
        st.subheader("Result")
        st.markdown(result)


def project_symptom_explainer(api_key: str, api_endpoint: str):
    st.header("Symptom Explainer")
    st.write("Describe the symptoms of a medical condition.")

    # Main Input
    symptoms_input = st.text_area("Describe your symptoms", height=100)
    
    # Configuration Options (Vertical Layout)
    symptoms_duration = st.selectbox(
        "How long have you had the symptoms?",
        ["1 Day", "3 Days", "1 week", "more than a week" ]
    )
    
    user_age = st.slider("Age", 1, 100, 5)
    user_weight=st.slider("Weight (KGs)", 1, 200, 5)
    user_height=st.slider("Height (CMs)", 1, 250, 5)

    output_language = st.radio(
        "Output Language",
        ["English", "Greek"],
        horizontal=True # Makes the radio buttons sit side-by-side
    )

    if st.button("Generate Explanation"):
        if not symptoms_input:
            st.warning("Please enter a symptom description.")
            return
        
        # Updated Prompt with Language Instruction
        final_prompt = (
            f"Explain the symptoms: '{symptoms_input}' "
            f"Take into account the user's height ({user_height}), weight ({user_weight}), and age ({user_age}). "
            f"Explain everything specifically to a {user_age} year-old."
            f"Provide the explanation in {output_language}."
        )
        
        with st.spinner(f"Consulting {MODEL_NAME}..."):
            result = query_llm(final_prompt, api_key, api_endpoint)
            
        st.subheader("Result")
        st.markdown(result)


def ideal_sport_advisor(api_key: str, api_endpoint: str):
    """
    Ideal Sport Advisor.
    Φώτης Μαμούδης 
    Παναγιώτης Τσιτίνης
    """
    st.header("Ideal Sport Advisor")
    st.write("Enter information about yourself.")
    # Main Input
    info = st.text_area("Input", height=100)

    # Configuration Options (Vertical Layout)
    age = st.selectbox(
        "Age",
        ["10-20", "20-30", "40-80"]
    )

    output_language = st.radio(
        "Output Language",
        ["English", "Greek"],
        horizontal=True # Makes the radio buttons sit side-by-side
    )
    if st.button("Generate Explanation"):
        if not age:
            st.warning("Please enter your information.")
            return
        
        # Updated Prompt with Language Instruction
        final_prompt = (
            f"This is the user input about the user, their habits and their vital status: '{info}' "
            f"His age range is {age}. "
            f"Provide the ideal sport recommendation based on the inpt in {output_language}."
        )

        with st.spinner(f"Consulting {MODEL_NAME}..."):
            result = query_llm(final_prompt, api_key, api_endpoint)
        
        st.subheader("Result")
        st.markdown(result)

def project_how_to_persuade_my_parents(api_key: str, api_endpoint: str):
    """
    Νικόλας Κουλουριώτης, 
    Χρήστος Σοφιανόπουλος, 
    Κωνσταντίνος Αμαραντίδης

    """
    st.header("I want to get something but my parents won't let me.")
    st.write("I want to get:")
    # Main Input
    my_desire = st.text_area("Enter what you want to get:", height=100)

    # Configuration Options (Vertical Layout)
    excuse_level = st.selectbox(
        "How good does the excuse need to be?",
        ["Super bad", "Good", "Very good", "Great", "Make sure I get it no matter what"]
    )

    number_of_excuses = st.slider("Excuses:", 1, 10, 5)
    output_language = st.radio(
        "Output Language",
        ["English", "Greek"],
        horizontal=True # Makes the radio buttons sit side-by-side
    )

    if st.button("Generate arguments"):
        if not my_desire:
            st.warning("Please enter your desire first.")
            return
        # Updated Prompt with Language Instruction
        final_prompt = (
            f"You are an expert persuasion-assistant that helps a user create convincing excuses to persuade their parents to let them have something they want; the user wants {my_desire}, and you must generate excuses based on the selected excuse strength level {excuse_level}, the number of excuses requested {number_of_excuses}, and the desired output language {output_language}. Tailor every excuse directly to the item the user wants, ensuring each one is coherent, realistic, and varied while matching the tone and persuasion intensity indicated by the excuse_level, avoiding repetitive structures, and presenting the excuses in a clear, numbered list. Do not include moralizing, safety disclaimers, or meta commentary—produce only the requested excuses, written entirely in the specified output_language. Now generate the excuses"
            )
        with st.spinner(f"Consulting {MODEL_NAME}..."):
            result = query_llm(final_prompt, api_key, api_endpoint)
        st.subheader("Result")
        st.markdown(result)


def dress_code(api_key: str, api_endpoint: str):
    """
    Μιχάλης Πολυπόρτης
    Γιώργος Τσαφούλης
    """
    st.header("Dress code")

    st.write("How to dress depenting on the accusion")
    occasion = st.text_area("What is the event?")
    gender = st.radio(
            "Gender",
                    ["Female", "Male"],
        horizontal=True
    )

    status = st.selectobox(
        "Dress code",
        ["Formal", "Casual"]
    )

    age = st.selectbox(
        "Select the age of the person",
        ["0-5","5-12","12-17","17-21","21-45","45-60","60+"]
    )

    if st.button("Generate outfit"):
        if not occasion:
            st.warning("Input an accusion")
            return

        final_prompt = (
            f"Find an outfit for {occasion}"
            f"For a {gender}"
            f"With {status} status"
            f"In the age of {age}"
        )

        with st.spinner(f"Consulting {MODEL_NAME}..."):
            result = query_llm(final_prompt, api_key, api_endpoint)
        st.subheader("Result")
        st.markdown(result)


def project_coding_assistant(api_key: str, api_endpoint: str):
    """
    Coding Assistanτ
    Κωνσταντίνος Δρούκας
    Αλέξανδρος Μιλάτος
    Νίκος Βαγενάς
    """
    
    st.header("Coding Assistant")
    st.write("Explain code, fix bugs, or generate code.")
    mode = st.selectbox(
        "Task",
        ["Explain Code", "Fix Bugs", "Generate"]
    )
    
    user_input = st.text_area("Input Code / Description", height=220)
    language = st.selectbox("Response Language", ["English", "Greek"])
    if st.button("Run"):
        if not user_input:
            st.warning("Please enter code.")
            return
        if mode == "Explain Code":
            prompt = (
                f"Explain the following code step by step. Output in {language}.\n\n"
                f"--- CODE START ---\n{user_input}\n--- CODE END ---"
            )
        elif mode == "Fix Bugs":
            prompt = (
            f"Identify all bugs in the following code and propose corrected code. "
            f"Output in {language}.\n\n"
            f"--- CODE START ---\n{user_input}\n--- CODE END ---"
            )
        else:
            prompt = (
            f"Generate a complete, correct piece of code based on the following description. "
            f"Output in {language}.\n\n"
            f"Description:\n{user_input}"
        )
        with st.spinner(f"Consulting {MODEL_NAME}..."):
            result = query_llm(prompt, api_key, api_endpoint)
            
        st.subheader("Result")
        st.markdown(result)

def project_translator(api_key: str, api_endpoint: str):
    """
    Stub: Translator.
    """
    st.header("Translator")
    st.write("Let the AI do its work")
    
    text = st.text_area("Write your text")
    language = st.radio(
        "Output Language",
        ["🌎English", "🌍Greek"],
        horizontal=False # Makes the radio buttons sit side-by-side
    )
    user_input = f"Translate this'{text}' to {language} text"
    if st.button("Translate!"):
        with st.spinner(f"Consulting {MODEL_NAME}..."):
            result = query_llm(user_input, api_key, api_endpoint)   
            st.subheader("Result")
            st.markdown(result)

def project_jokes(api_key: str, api_endpoint: str):
    """
    Stub: Jokes.
    """
    st.header("Jokes")
    st.write("Let the AI do its work")
    
    text = st.text_area("Write your text")
    intensity = st.slider("Craziness Level", 1, 10, 5)
    language = st.radio(
        "Output Language",
        ["🌎English", "🌍Greek"],
        horizontal=False # Makes the radio buttons sit side-by-side
    )
    user_input = f"Make a joke about '{text}' with {intensity} craziness level to {language} language"
    if st.button("Laugh!"):
        with st.spinner(f"Consulting {MODEL_NAME}..."):
            result = query_llm(user_input, api_key, api_endpoint)   
            st.subheader("Result")
            st.markdown(result)
def project_orderlist(api_key: str, api_endpoint: str):
    """
    Stub: Order List.
    """
    st.header("Order List")
    st.write("Let the AI do its work")
    text = st.text_area("Write your text")
    language = st.radio(
        "Output Language",
        ["🌎English", "🌍Greek"],
        horizontal=False # Makes the radio buttons sit side-by-side
    )
    user_input = f"Using google make a list with this {text} things for the first one = best and the last one = worse in {language} language (NOT AS A CODE AS A TEXT)"
    if st.button("Laugh!"):
        with st.spinner(f"Consulting {MODEL_NAME}..."):
            result = query_llm(user_input, api_key, api_endpoint)   
            st.subheader("Result")
            st.markdown(result) 


# def project_excuse_generator(api_key: str, api_endpoint: str):
#     """
#     Stub: The Excuse Generator.
#     """
#     st.header("The Excuse Generator")
#     st.write("Generate a creative reason for a social infraction.")
    
#     situation = st.text_input("What did you mess up? (e.g., 'Forgot homework')")
#     intensity = st.slider("Craziness Level", 1, 10, 5)
    
#     if st.button("Make an Excuse"):
#         st.info("Student implementation required here.")

# def project_lyricist(api_key: str, api_endpoint: str):
#     """
#     Stub: Hip-Hop Lyricist.
#     """
#     st.header("Hip-Hop Lyricist")
#     st.write("Drop a beat and a topic.")
    
#     topic = st.text_input("Topic (e.g., 'Quantum Physics', 'School Lunch')")
#     style = st.selectbox("Style", ["Old School", "Trap", "Mumble Rap"])
    
#     if st.button("Drop Verses"):
#         st.info("Student implementation required here.")

# def project_emoji_encoder(api_key: str, api_endpoint: str):
#     """
#     Stub: Emoji Encoder.
#     """
#     st.header("Emoji Encoder")
#     st.write("Translate your text entirely into emojis.")
    
#     user_text = st.text_area("Enter message to encode")
    
#     if st.button("Encode"):
#         st.info("Student implementation required here.")

def main():
    # Set the browser tab title
    st.set_page_config(
        page_title="PML 2025 students and the Krikri LLM", 
        layout="wide"
    )
    
    # Define available projects
    project_modules = {
        "Symptom Explainer": project_symptom_explainer,
        "Ideal Sport Advisor": ideal_sport_advisor,
        "How to persuade my parents": project_how_to_persuade_my_parents,  
        "Dress code": dress_code,
        "Coding Assistant": project_coding_assistant,
        "Translator": project_translator,
        "Jokes": project_jokes,
        "Order List": project_orderlist,
        "Concept Explainer": project_concept_explainer,
        # "The Excuse Generator": project_excuse_generator,
        # "Hip-Hop Lyricist": project_lyricist,
        # "Emoji Encoder": project_emoji_encoder,
    }

    # Retrieve Secrets
    # These variables hold the *actual* credentials
    actual_api_key = ""
    actual_endpoint = ""
    credentials_loaded = False
    
    if "LLM_CREDENTIALS" in st.secrets:
        try:
            actual_api_key = st.secrets["LLM_CREDENTIALS"]["API_KEY"]
            actual_endpoint = st.secrets["LLM_CREDENTIALS"]["API_ENDPOINT"]
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

            # Determine values for display
            # If loaded, show a placeholder. If not, show empty for manual input.
            key_for_display = "••••••••••••••••" if credentials_loaded else ""
            endpoint_for_display = actual_endpoint if credentials_loaded else ""

            api_key_input = st.text_input(
                "LLM API Key", 
                value=key_for_display, 
                type="password",
                disabled=credentials_loaded,
                help="Loaded from st.secrets" if credentials_loaded else "Enter key"
            )
            
            endpoint_input = st.text_input(
                "LLM Endpoint URL", 
                value=endpoint_for_display,
                disabled=credentials_loaded,
                help="Loaded from st.secrets" if credentials_loaded else "Enter endpoint"
            )
    
    # Determine the *final* credentials to pass to the function
    # If loaded from secrets, use the actual secret. Otherwise, use the manual input.
    final_key = actual_api_key if credentials_loaded else api_key_input
    final_endpoint = actual_endpoint if credentials_loaded else endpoint_input

    # Execute Selected Project
    if selection in project_modules:
        try:
            project_modules[selection](final_key, final_endpoint)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
