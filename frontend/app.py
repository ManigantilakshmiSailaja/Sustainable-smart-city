import streamlit as st
import requests

# Set page config
st.set_page_config(page_title="Sustainable Smart City Assistant", layout="wide")

# ---------- Custom CSS for Styling ----------
st.markdown("""
    <style>
        .main-title {
            font-size: 45px;
            font-weight: bold;
            color: #0072ff;
            text-align: center;
            margin-bottom: 10px;
        }
        .sub-title {
            font-size: 22px;
            color: #333333;
            text-align: center;
            margin-bottom: 25px;
        }
        footer {visibility: hidden;}
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            color: #888888;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("<div class='main-title'>🌆 Sustainable Smart City Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Empowering Urban Governance with AI and LLMs 🚀</div>", unsafe_allow_html=True)

# ---------- Sidebar Navigation ----------
st.sidebar.title("🔍 Choose a Feature")
option = st.sidebar.radio("choose a section", [
    "Summarizer", "Forecast", "Eco Tips", "Citizen Feedback",
    "Chat Assistant", "Anomaly Detection"
], label_visibility="visible")

# ---------- Feature: Summarizer ----------
if option == "Summarizer":
    st.header("📄 Policy Document Summarizer")
    st.write("Upload a text file containing policy details.")
    file = st.file_uploader("Choose a `.txt` file", type=["txt"])
    if file and st.button("Summarize"):
        response = requests.post("http://localhost:8000/summarize/", files={"file": file})
        st.success(response.json()["summary"])

# ---------- Feature: Forecast ----------
elif option == "Forecast":
    st.header("📊 KPI Forecasting")
    st.write("Upload a KPI CSV file (e.g., year & value) to predict next year's performance.")
    file = st.file_uploader("Choose a `.csv` file", type=["csv"])
    if file and st.button("Forecast"):
        response = requests.post("http://localhost:8000/forecast/", files={"file": file})
        st.success(f"📈 Predicted KPI: {response.json()['next_year_prediction']}")

# ---------- Feature: Eco Tips ----------
elif option == "Eco Tips":
    st.header("🌱 Eco Tips Generator")
    st.write("Type a keyword like 'plastic', 'water', or 'energy' to get sustainability tips.")
    keyword = st.text_input("Enter keyword")
    if st.button("Get Tip"):
        response = requests.get("http://localhost:8000/eco", params={"keyword": keyword})
        st.info(response.json()["tip"])

# ---------- Feature: Citizen Feedback ----------
elif option == "Citizen Feedback":
    st.header("📢 Report a City Issue")
    st.write("Submit feedback about any issue in your locality.")
    name = st.text_input("Your Name")
    issue = st.text_area("Describe the issue")
    category = st.selectbox("Category", ["Water", "Electricity", "Sanitation", "Roads", "Other"])
    if st.button("Submit Feedback"):
        data = {"name": name, "issue": issue, "category": category}
        response = requests.post("http://localhost:8000/feedback/", data=data)
        st.success(response.json()["message"])

# ---------- Feature: Chat Assistant ----------
elif option == "Chat Assistant":
    st.header("💬 Smart City Chat Assistant")
    st.write("Ask any question about smart city strategies, carbon reduction, green living, etc.")
    question = st.text_input("Ask something...")
    if st.button("Ask"):
        response = requests.get("http://localhost:8000/chat", params={"question": question})
        st.success(response.json()["answer"])

# ---------- Feature: Anomaly Detection ----------
elif option == "Anomaly Detection":
    st.header("⚠️ Energy Usage Anomaly Detector")
    st.write("Upload a CSV with `Zone` and `Usage` columns to detect abnormal energy consumption.")
    file = st.file_uploader("Choose a `.csv` file", type=["csv"])
    if file and st.button("Detect Anomalies"):
        response = requests.post("http://localhost:8000/anomaly/", files={"file": file})
        anomalies = response.json()["anomalies"]
        if anomalies:
            st.error("🚨 Anomalies Detected:")
            st.write(anomalies)
        else:
            st.success("✅ No anomalies found.")

# ---------- Footer ----------
st.markdown("""
    <div class='footer'>Built by Sailaja Maniganti | Internship Project | Powered by Hugging Face & FastAPI</div>
""", unsafe_allow_html=True)
