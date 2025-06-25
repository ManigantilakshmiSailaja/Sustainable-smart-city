# Sustainable Smart City Assistant

A prototype AI tool for summarizing city policies, forecasting KPIs, and giving eco-tips.

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run FastAPI backend:
   cd backend
   uvicorn main:app --reload

3. Run Streamlit frontend:
   cd frontend
   streamlit run streamlit_app.py

## Features

- Policy Summarization using LLM (mocked)
- KPI Forecasting with Linear Regression
- Eco Tips Generation

Use this as a foundation to integrate real IBM Watsonx Granite LLM and Pinecone later.
