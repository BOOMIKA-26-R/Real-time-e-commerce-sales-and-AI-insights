import streamlit as st
import requests
import pandas as pd
import time

st.set_page_config(page_title="E-Comm AI Dashboard", layout="wide")
st.title("🚀 Real-Time E-Commerce AI Insights")


BASE_URL = "https://real-time-e-commerce-sales-and-ai.onrender.com"

threshold = st.sidebar.number_input("Revenue Alert Threshold ($)", value=300)

st.sidebar.markdown("---")
st.sidebar.subheader("Admin Controls")
if st.sidebar.button("Retrain AI Model"):
    with st.spinner("Retraining on latest data..."):
        try:

            retrain_res = requests.post(f"{BASE_URL}/retrain").json()
            st.sidebar.success(retrain_res["message"])
            time.sleep(2)
        except Exception as e:
            st.sidebar.error(f"Retrain failed: {e}")

if st.sidebar.button("Refresh Live Data"):
    try:

        data_res = requests.get(f"{BASE_URL}/live-data").json()
        

        traffic_val = data_res['traffic']
        pred_res = requests.get(f"{BASE_URL}/predict?traffic={traffic_val}").json()
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Live Sale", f"${data_res['sales']}")
        col2.metric("Predicted Revenue", f"${pred_res['predicted_revenue']:.2f}")
        col3.metric("Customer Sentiment", f"{data_res['customer_sentiment']:.2f}")

        if data_res['sales'] > threshold:
            st.warning(f"🔥 High Value Sale Detected in {data_res['category']}!")
            
    except Exception as e:
        st.error(f"Connection Error: Check Render Logs. Details: {e}")

st.info(f"Connected to API at: {BASE_URL}")
