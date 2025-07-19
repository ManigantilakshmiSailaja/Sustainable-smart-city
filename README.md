# Sustainable Smart City Assistant using IBM Granite LLM 🌱🏙️

## 🚀 Project Overview

This project is developed as part of the **SmartBridge Generative AI Virtual Internship**. The aim is to build a **Sustainable Smart City Assistant** that helps citizens interact with their city's resources using an intelligent AI interface powered by **IBM Watsonx Granite LLM**.

The assistant can answer sustainability-related questions, suggest eco-friendly practices, provide weather updates, and support smart city interactions like transport, waste management, and energy conservation.

---

## 📚 Project Phases Breakdown

### 🔹 Phase 1: Ideation and Research
- Finalized the concept of a Smart City Assistant that focuses on **sustainability** and **AI-driven interaction**.
- Researched IBM Granite LLM and Hugging Face models.
- Selected technologies: `Streamlit`, `FastAPI`, `Hugging Face`, `IBM Watsonx`, and optionally `Pinecone`.

### 🔹 Phase 2: Dataset Preparation and LLM Setup
- Integrated a large language model (**Falcon-7B-Instruct**) as a base due to IBM Granite's availability constraints.
- Used `.safetensors` model files:  
  - `model-00001-of-00002.safetensors`  
  - `model-00002-of-00002.safetensors`
- Loaded and used models via Transformers and Hugging Face `pipeline`.

### 🔹 Phase 3: Application Development
- Developed a simple, interactive **Streamlit-based front-end**.
- Set up a `FastAPI` (or Flask) backend to interact with the LLM and process inputs.
- Integrated modular components:
  - Natural language input
  - Response generation from LLM
  - Optional weather API support (OpenWeather or similar)
  - Eco tips / smart suggestions
  - City development facts or government initiatives

### 🔹 Phase 4: Final Integration & Deployment
- Deployed locally due to model size.
- Ensured clean UI with easy prompt input and clear assistant output.
- Recorded demo video and hosted final codebase on GitHub.

---

## 🧠 Tech Stack

| Area              | Technology Used              |
|-------------------|------------------------------|
| Frontend UI       | Streamlit                    |
| Backend API       | FastAPI / Flask              |
| LLM               | Falcon-7B-Instruct / IBM Granite |
| Model Source      | Hugging Face (Offline Setup) |
| Model Format      | `.safetensors`               |
| Language          | Python                       |

---

## 📦 Directory Structure

smart-city-assistant/
├── app.py
├── backend/
│ └── api.py
├── models/
│ ├── config.json
│ ├── model-00001-of-00002.safetensors
│ ├── model-00002-of-00002.safetensors
│ └── tokenizer/
├── templates/
│ └── ui.html
├── README.md
└── requirements.txt

yaml
Copy
Edit

---

## 📽️ Project Demonstration Video

👉 [Click to watch the demo video](https://drive.google.com/drive/folders/1m_vXdKkujfkVq1x57h6bZ3Kj_07hdh4T?usp=sharing)

---

## ✅ How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
Run Streamlit App:
streamlit run app.py

streamlit run app.py
Optional Backend:
If using FastAPI:
uvicorn backend.api:app --reload
Model Setup:
Ensure you have the following files inside models/ folder:

model-00001-of-00002.safetensors

model-00002-of-00002.safetensors

config.json, tokenizer/ etc.

📌 Key Features
💡 Ask sustainability-related questions in natural language

🌤️ Get real-time weather & smart city info

🧠 Powered by Hugging Face LLM models offline

🛠️ Easy to use with Streamlit UI

♻️ Built with sustainability at its core

🙏 Acknowledgements
SmartBridge for hosting this Generative AI Internship

IBM Watsonx and Hugging Face for LLM access

Mentors and reviewers for their support

📅 Submission Details
Student Name: Sailaja Maniganti

Project Title: Sustainable Smart City Assistant

Internship: SmartBridge - Generative AI Virtual Internship

Re-submission: ✅ Updated with complete files and demo video
