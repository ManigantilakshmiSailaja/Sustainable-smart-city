# 🌆 Sustainable Smart City Assistant

## 📽️ Demonstration Video
[Watch Demo Video](https://drive.google.com/file/d/1_W4fZmvpxNki0SbtjuQHNGjy9JsOaNoX/view?usp=sharing)

---

## 🧠 Project Overview

The **Sustainable Smart City Assistant** is an AI-powered citizen engagement platform built to support sustainability, governance, and real-time interaction between citizens and authorities in smart cities.

It combines Generative AI capabilities from Hugging Face with user-friendly interfaces through Streamlit and FastAPI. This platform allows citizens to interact intelligently and get responses related to city services, environmental data, and sustainable initiatives.

---

## 🚀 Features

- 💬 **AI-Powered Assistant**: Uses Hugging Face language models to generate human-like responses.
- 🌍 **Sustainability Focus**: Encourages eco-friendly behaviors and provides info on smart city initiatives.
- ⚡ **FastAPI Backend**: Provides API services for the AI assistant and external integrations.
- 🖼️ **Streamlit Frontend**: Interactive UI for users to chat and receive responses.
- 📊 **Real-time Feedback**: Citizens can get insights and make informed choices.

---

## 🧰 Technologies Used

| Tech         | Purpose                            |
|--------------|-------------------------------------|
| Python       | Core programming language          |
| Streamlit    | Frontend for the AI chat interface |
| FastAPI      | Backend server for APIs            |
| Hugging Face | Pre-trained LLMs for Generative AI |
| HTML/CSS     | Minor styling and formatting       |

---

## 📁 Project Structure

Sustainable-smart-city-assistant/
│
├── backend/ # FastAPI app with routes and Hugging Face model integration
│ └── main.py
│
├── frontend/ # Streamlit frontend app
│ └── app.py
│
├── models/ # Optional (you may delete large downloaded models)
│
├── documentation/ # Contains the project documentation files (.docx, .pdf)
│
├── requirements.txt # Python dependencies
├── README.md # Project README (this file)

yaml
Copy
Edit

---

## 🧠 Hugging Face Models

This project uses language models manually downloaded from [Hugging Face](https://huggingface.co/). Make sure you **do not push large model files** to GitHub.

If needed, models can be downloaded and cached using the Hugging Face `transformers` library.

---

## ⚙️ Installation & Run

### 🔧 Step 1: Clone Repository
```bash
git clone https://github.com/your-username/Sustainable-smart-city-assistant.git
cd Sustainable-smart-city-assistant
📦 Step 2: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🚀 Step 3: Run Backend (FastAPI)
bash
Copy
Edit
cd backend
uvicorn main:app --reload
🖥️ Step 4: Run Frontend (Streamlit)
bash
Copy
Edit
cd frontend
streamlit run app.py
❗ Notes
Do not upload model files directly if they exceed GitHub’s limits (use .gitignore).

Make sure your documentation files are inside the /documentation folder.

If your project exceeds the GitHub file size limit, compress large folders (except models) or use Drive for model sharing.

📜 License
This project is for educational use as part of the SmartBridge AI Internship.

👤 Author
Maniganti Lakshmi Sailaja
Final Year Student, St. Mary’s Women’s Engineering College
GitHub: ManigantilakshmiSailaja

yaml
Copy
Edit

---

### ✅ What to Do Next:

1. Save the above code as a file named `README.md` inside your GitHub repo.
2. Make sure `documentation/` contains your `.docx` or `.pdf` files.
3. Ensure large files (over 100MB) are not committed—especially models.
4. Push the latest version of your repo with commit message like:
git add .
git commit -m "Final project re-submission with documentation and video link"
git push origin main



Let me know if you'd like a ZIP-ready version or help writing your final commit.
