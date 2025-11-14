# Προτάσεις Μαθητικών Έργων (Με Branding)

## Επισκόπηση Αλλαγών

-   Προσθήκη του λογότυπου μέσω της συνάρτησης `st.image` στην πλευρική στήλη
-   Εισαγωγή του τίτλου "PML 2025 students" κάτω από το λογότυπο
-   Διατήρηση της ελληνικής γλώσσας για το υπόλοιπο περιβάλλον εργασίας

## Κώδικας Εφαρμογής Streamlit

```python
import streamlit as st
import logging

# Ρύθμιση καταγραφής
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def query_llm(prompt: str, api_key: str) -> str:
    """
    Κεντρική συνάρτηση για τη διαχείριση κλήσεων στο API του LLM.
    """
    if not api_key:
        raise ValueError("Το κλειδί API λείπει")
    
    try:
        # Προσομοίωση επιστροφής για επίδειξη
        logger.info(f"Mock LLM call executed for prompt: {prompt[:30]}...")
        return f"Προσομοιωμένη απάντηση LLM για: {prompt}"
        
    except Exception as e:
        logger.error(f"Αποτυχία κλήσης API: {e}")
        return "Σφάλμα: Αδυναμία ανάκτησης απάντησης από το LLM."

def project_concept_explainer(api_key: str):
    """
    Πλήρης Υλοποίηση: Επεξηγητής Εννοιών.
    """
    st.header("Επεξηγητής Εννοιών")
    st.write("Εισάγετε μια σύνθετη έννοια και επιλέξτε το κοινό-στόχο.")

    topic_input = st.text_area("Εισάγετε την έννοια προς επεξήγηση", height=100)
    complexity_level = st.selectbox(
        "Κοινό Στόχος",
        ["Πεντάχρονο παιδί", "Μαθητής Λυκείου", "Καθηγητής Πανεπιστημίου"]
    )

    if st.button("Δημιουργία Επεξήγησης"):
        if not topic_input:
            st.warning("Παρακαλώ εισάγετε ένα θέμα πρώτα.")
            return
        
        final_prompt = (
            f"Εξήγησε την έννοια '{topic_input}' "
            f"συγκεκριμένα σε ένα {complexity_level}."
        )
        
        with st.spinner("Επικοινωνία με το LLM..."):
            result = query_llm(final_prompt, api_key)
            
        st.subheader("Αποτέλεσμα")
        st.markdown(result)

def project_excuse_generator(api_key: str):
    """
    Στέλεχος (Stub): Γεννήτρια Δικαιολογιών.
    """
    st.header("Γεννήτρια Δικαιολογιών")
    st.write("Δημιουργήστε μια δικαιολογία για μια κοινωνική παράβαση.")
    
    situation = st.text_input("Τι πήγε στραβά; (π.χ. 'Ξέχασα τις ασκήσεις')")
    intensity = st.slider("Επίπεδο Τρέλας", 1, 10, 5)
    
    if st.button("Φτιάξε Δικαιολογία"):
        st.info("Απαιτείται υλοποίηση από τον μαθητή.")

def project_lyricist(api_key: str):
    """
    Στέλεχος (Stub): Στιχουργός Χιπ-Χοπ.
    """
    st.header("Στιχουργός Χιπ-Χοπ")
    st.write("Δώστε ρυθμό και θέμα.")
    
    topic = st.text_input("Θέμα (π.χ. 'Κβαντική Φυσική', 'Σχολικό Κυλικείο')")
    style = st.selectbox("Στυλ", ["Old School", "Trap", "Mumble Rap"])
    
    if st.button("Δημιουργία Στίχων"):
        st.info("Απαιτείται υλοποίηση από τον μαθητή.")

def project_emoji_encoder(api_key: str):
    """
    Στέλεχος (Stub): Κωδικοποιητής Emoji.
    """
    st.header("Κωδικοποιητής Emoji")
    st.write("Μεταφράστε το κείμενό σας αποκλειστικά σε emojis.")
    
    user_text = st.text_area("Εισάγετε μήνυμα για κωδικοποίηση")
    
    if st.button("Κωδικοποίηση"):
        st.info("Απαιτείται υλοποίηση από τον μαθητή.")

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
            st.write("Hellenic American Union") # Fallback text
            
        st.title("PML 2025 students")
        st.divider()
        
        # Configuration Section
        st.subheader("Ρυθμίσεις")
        api_key = st.text_input("Εισάγετε Κλειδί API LLM", type="password")
        st.divider()
        st.subheader("Επιλογή Εφαρμογής")
    
    # Λεξικό Επιλογής
    project_modules = {
        "Επεξηγητής Εννοιών": project_concept_explainer,
        "Γεννήτρια Δικαιολογιών": project_excuse_generator,
        "Στιχουργός Χιπ-Χοπ": project_lyricist,
        "Κωδικοποιητής Emoji": project_emoji_encoder
    }
    
    selection = st.sidebar.radio("Διαθέσιμα Εργαλεία:", list(project_modules.keys()))
    
    if selection in project_modules:
        current_function = project_modules[selection]
        try:
            current_function(api_key)
        except Exception as e:
            st.error(f"Παρουσιάστηκε σφάλμα στην ενότητα: {e}")
            logger.error(f"Module execution error: {e}")

if __name__ == "__main__":
    main()
