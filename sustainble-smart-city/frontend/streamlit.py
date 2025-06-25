# app.py

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart City Assistant", layout="centered")

# Title and Navigation
st.title("🌆 Sustainable Smart City Assistant")
module = st.sidebar.selectbox(
    "📚 Select a Module",
    [
        "🏠 Home",
        "📘 Policy Summarization",
        "📣 Citizen Feedback",
        "📈 KPI Forecasting",
        "🌱 Eco Tips",
        "💬 Chat Assistant"
    ]
)

# 1. Home Page
if module == "🏠 Home":
    st.header("🏙️ About the Project")
    st.markdown("""
    The Sustainable Smart City Assistant is an AI-powered platform that:
    - Summarizes city policies using LLMs
    - Collects citizen feedback
    - Forecasts KPIs with ML
    - Shares eco-friendly tips
    - Detects anomalies
    - Answers public queries
    """)

# 2. Policy Summarization
elif module == "📘 Policy Summarization":
    st.header("📘 Upload Policy Document")
    uploaded_file = st.file_uploader("Upload .txt file", type="txt")
    if uploaded_file:
        policy_text = uploaded_file.read().decode("utf-8")
        st.text_area("📄 Original Text", policy_text, height=200)
        if st.button("🧠 Summarize"):
            st.success("📌 Summary:\n\n[LLM-based summary will appear here]")

# 3. Citizen Feedback
elif module == "📣 Citizen Feedback":
    st.header("📣 Submit Feedback")
    category = st.selectbox("Category", ["Water", "Electricity", "Road", "Others"])
    message = st.text_area("Describe the issue:")
    if st.button("📤 Submit"):
        with open("feedback.csv", "a") as f:
            f.write(f"{category},{message}\n")
        st.success("✅ Your feedback has been recorded!")

# 4. KPI Forecasting
elif module == "📈 KPI Forecasting":
    st.header("📈 KPI Forecasting Tool")
    file = st.file_uploader("Upload a CSV (with Year and Usage columns)", type="csv")
    if file:
        df = pd.read_csv(file)
        st.write("Uploaded Data:")
        st.dataframe(df)
        st.success("📊 Forecast Result:\n\n[Linear Regression result will show here]")

# 5. Eco Tips
elif module == "🌱 Eco Tips":
    st.header("🌱 Get Eco Tips")
    keyword = st.text_input("Enter a topic (e.g., solar, plastic)")
    if st.button("🌍 Generate Tip"):
        st.info("Tip: [Eco advice will appear here based on the keyword]")

# 6. Chat Assistant
elif module == "💬 Chat Assistant":
    st.header("💬 Ask the Assistant")
    query = st.text_input("Your question about sustainability or smart cities:")
    if st.button("Ask"):
        st.success("🤖 Response: [LLM-based answer will appear here]")
