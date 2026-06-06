import streamlit as st
import os

st.set_page_config(page_title="cryptoML Dashboard", layout="wide")
st.title("🔒 cryptoML - Federated Anomaly Detection")

st.sidebar.success("Connected to Federation Server")

col1, col2 = st.columns(2)
with col1:
    st.metric("Active Agencies", "2/2")
    st.metric("FL Rounds Completed", "3")

with col2:
    st.metric("Global Model Loss", "0.042")
    st.metric("Anomalies Detected (last 24h)", "7")

st.subheader("Recent Anomalies")
st.write("Sample alerts would appear here (connected to agencies).")

if st.button("Trigger New FL Round"):
    st.success("New federation round started!")

st.caption("Privacy Preserved • No raw logs shared")