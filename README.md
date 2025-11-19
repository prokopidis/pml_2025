# PML 2025 - Krikri LLM Student Projects

A collection of interactive AI-powered applications built with Streamlit and the Krikri LLM API. This project showcases various student-created tools that leverage large language models for educational and creative purposes.

## 🚀 Features

This application includes the following modules:

### **Symptom Explainer**

* Γιώργος Τσαφούλης, Φώτης Μαμούδης

Get personalized medical insights by describing your symptoms. The tool considers your age, height, weight, and symptom duration to provide contextual explanations in your preferred language.

### **Ideal Sport Advisor**

* Φώτης Μαμούδης, Παναγιώτης Τσιτίνης

Receive personalized sport recommendations based on your age, habits, and vital status. Get advice tailored to your age group and lifestyle.

### **How to Persuade My Parents**

* Νικόλας Κουλουριώτης, Χρήστος Σοφιανόπουλος & Κωνσταντίνος Αμαραντίδης

Generate convincing arguments to help you persuade your parents. Adjust the excuse strength level and get multiple tailored arguments for what you want.

### **Dress Code Advisor**

* Μιχάλης Πολυπόρτης & Γιώργος Τσαφούλης

Get outfit recommendations based on the occasion, gender, dress code formality, and age group. Perfect for any event!

### **Coding Assistant**

* Κωνσταντίνος Δρούκας, Αλέξανδρος Μιλάτος & Νίκος Βαγενάς

Your AI programming companion with three modes:

* **Explain Code**: Get step-by-step explanations of code
* **Fix Bugs**: Identify bugs and receive corrected code
* **Generate**: Create new code from descriptions

### **Translator**

* Ευαγγελία Κορκοβέλου, Θωμάς Τσολάκης

Quickly translate text between English and Greek with AI-powered accuracy.

### **Jokes Generator**

* Ευαγγελία Κορκοβέλου, Θωμάς Τσολάκης

Create hilarious jokes on any topic with adjustable craziness levels. Get your humor in English or Greek!

### **Order List**

* Ευαγγελία Κορκοβέλου, Θωμάς Τσολάκης

Generate ranked lists of items ordered from best to worst based on your criteria and preferred language.

## 🛠️ Installation

1. **Clone or download** this repository
2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure credentials** in `.streamlit/secrets.toml`:

   ```toml
   [LLM_CREDENTIALS]
   API_KEY = "your-api-key"
   API_ENDPOINT = "your-endpoint-url"
   ```

## ▶️ Running the Application

Start the Streamlit app:

```bash
streamlit run streamlit_app.py
```

The app will open in your default browser at `http://localhost:8501`.

## 📋 Requirements

* Python >= 3.12
* streamlit >= 1.30.0
* openai >= 1.0.0

See [requirements.txt](requirements.txt) for complete dependencies.

## 📁 Project Structure

```
pml_2025/
├── streamlit_app.py          # Main application with all modules
├── main.py                   # Entry point stub
├── requirements.txt          # Python dependencies
├── pyproject.toml           # Project metadata
├── .python-version          # Python 3.12
├── .streamlit/
│   └── secrets.toml         # API credentials (gitignored)
└── README.md                # This file
```

## 🎓 About

This project is developed by PML 2025 students using the Krikri LLM API. Each module demonstrates different applications of large language models in education, wellness, creativity, and problem-solving.

---

**Built with ❤️ by PML 2025 Students**
