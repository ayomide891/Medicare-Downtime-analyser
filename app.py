import streamlit as st
import pandas as pd
from datetime import datetime
import io

# PAGE CONFIG
st.set_page_config(
    page_title="MEDCARE LABS - Downtime Analyzer",
    page_icon="🏥",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #0066CC 0%, #004499 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background-color: #0066CC;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-size: 16px;
        font-weight: bold;
    }
    .footer {
        text-align: center;
        color: #666;
        padding: 2rem;
        margin-top: 3rem;
        border-top: 1px solid #eee;
    }
</style>
""", unsafe_allow_html=True)

# SESSION STATE FOR PAGE NAVIGATION
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

# LANDING PAGE
if st.session_state.page == 'landing':
    st.markdown('<div class="main-header"><h1>🏥 MEDCARE LABS</h1><h3>Downtime Analyzer & Report Generator</h3></div>', unsafe_allow_html=True)
    
    st.write("### Welcome!")
    st.write("Track machine downtime, calculate total hours, and generate professional reports for ANY hospital or lab.")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("
