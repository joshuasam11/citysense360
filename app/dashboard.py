import streamlit as st
import cv2
import numpy as np
from traffic_model import predict_next
from cctv_detection import run_detection
from complaint_analyzer import classify_complaint, summarize
from rag_chatbot import build_index, answer_question
import sys, os
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from agents.city_agents import run_agents   # keep since it's working for you

st.set_page_config(page_title="CitySense360", layout="wide")

st.title("🌆 CitySense360 — Smart City AI Dashboard")

API_BASE = "https://citysense360-api.onrender.com"   # <-- your deployed API


tab1, tab2, tab3, tab4 = st.tabs([
    "Traffic Prediction",
    "CCTV Detection",
    "Complaint Analyzer",
    "City Chatbot"
])


# ---------------- TRAFFIC PREDICTION ----------------
with tab1:
    st.header("Traffic Congestion Prediction")

    st.write("Enter last 3 recorded vehicle counts:")

    c1, c2, c3 = st.columns(3)
    v1 = c1.number_input("Count 1", value=30)
    v2 = c2.number_input("Count 2", value=50)
    v3 = c3.number_input("Count 3", value=70)

    if st.button("Predict Congestion Level", key="traffic_api_button"):
        try:
            response = requests.get(
                f"{API_BASE}/predict/traffic",
                params={"v1": v1, "v2": v2, "v3": v3},
                timeout=20
            )

            result = response.json()["prediction"]
            st.success(f"Predicted next traffic count: {result} vehicles")

        except Exception as e:
            st.error("⚠️ Unable to connect to API. Please try again.")
            st.code(str(e))


# ---------------- CCTV DETECTION ----------------
with tab2:
    st.header("AI CCTV Monitoring")

    uploaded = st.file_uploader("Upload CCTV image", type=["jpg", "png", "jpeg"])

    if uploaded:
        st.image(uploaded, caption="Uploaded Frame", width=500)

        if st.button("Run Detection"):
            output = run_detection(uploaded)
            st.image(output, caption="Detection Output", width=600)


# ---------------- COMPLAINT ANALYZER ----------------
with tab3:
    st.header("Citizen Complaints Analyzer")

    complaint = st.text_area("Enter complaint text here")

    if st.button("Analyze Complaint"):
        category = classify_complaint(complaint)
        short = summarize(complaint)

        st.success(f"Category detected: **{category}**")
        st.write("Summary:")
        st.info(short)


# ---------------- CHATBOT (RAG) ----------------
with tab4:
    st.header("City Information Chatbot (RAG)")

    context = st.text_area("Paste city policy / rules / document text here")

    if "rag_index" not in st.session_state:
        st.session_state.rag_index = None
        st.session_state.rag_chunks = None

    if st.button("Build Knowledge Base"):
        idx, ch = build_index(context)
        st.session_state.rag_index = idx
        st.session_state.rag_chunks = ch
        st.success("Knowledge base created!")

    question = st.text_input("Ask a question")

    if st.button("Get Answer"):
        if st.session_state.rag_index:
            reply = answer_question(
                st.session_state.rag_index,
                st.session_state.rag_chunks,
                question
            )
            st.info(reply)
        else:
            st.warning("Please build the knowledge base first.")


# ---------------- AI CITY AGENTS ----------------
st.subheader("AI City Operations Agent")

task = st.text_input("Describe a city operation task (example: plan garbage collection)")

if st.button("Run AI Agents"):
    plan, data, report = run_agents(task)

    st.write("🧭 Plan:")
    st.info(plan)

    st.write("📊 Data Step:")
    st.warning(data)

    st.write("📑 Final Report:")
    st.success(report)
