import streamlit as st
import pandas as pd
import numpy as np
from engine import QuantaFlowEngine

st.set_page_config(page_title="QuantaFlow AI", layout="wide")

st.title("🚀 QuantaFlow: Autonomous Data Cleaning")
st.markdown("### *Developed by Aditya Singh (MCA)*")

# Sidebar for project info
st.sidebar.header("Project Details")
st.sidebar.info("QuantaFlow uses IQR for outlier removal and automated imputation for missing values.")

# 1. File Upload Section
uploaded_file = st.file_uploader("Upload your 'Dirty' CSV file", type=["csv"])

if uploaded_file is not None:
    # Save file temporarily
    with open("temp_upload.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Initialize Engine
    qf = QuantaFlowEngine("temp_upload.csv")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Original Data")
        st.dataframe(qf.df)
        
    # 2. Action Button
    if st.button("✨ Run Intelligent Cleaning"):
        qf.auto_audit()
        qf.smart_impute()
        
        # Clean Marks and Encode City automatically
        if 'Marks' in qf.df.columns:
            qf.remove_outliers('Marks')
        if 'City' in qf.df.columns:
            qf.encode_categorical('City')
            
        with col2:
            st.subheader("✅ Cleaned Data")
            st.dataframe(qf.df)
            
            st.success("Cleaning Pipeline Executed Successfully!")
            st.text_area("Execution Log:", qf.get_final_report(), height=150)
            
            # 3. Download Clean Data
            csv = qf.df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Cleaned CSV",
                data=csv,
                file_name="QuantaFlow_Cleaned.csv",
                mime="text/csv",
            )