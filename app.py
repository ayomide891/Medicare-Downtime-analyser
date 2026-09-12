import streamlit as st
import pandas as pd
from datetime import datetime
import io

st.set_page_config(page_title="MEDCARE LABS", page_icon="🏥", layout="wide")

# CSS - FIXED QUOTES
st.markdown("""
<style>
.main-header {background: linear-gradient(90deg, #0066CC 0%, #004499 100%); padding: 2rem; border-radius: 10px; color: white; text-align: center; margin-bottom: 2rem;}
.stButton>button {background-color: #0066CC; color: white; border-radius: 8px; height: 3em; width: 100%; font-size: 16px; font-weight: bold;}
.footer {text-align: center; color: #666; padding: 2rem; margin-top: 3rem; border-top: 1px solid #eee;}
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'landing'

# LANDING PAGE
if st.session_state.page == 'landing':
    st.markdown('<div class="main-header"><h1>🏥 MEDCARE LABS</h1><h3>Downtime Analyzer</h3></div>', unsafe_allow_html=True)
    st.write("### Welcome!")
    st.write("Track machine downtime and generate reports for ANY hospital.")
    
    if st.button("🚀 Get Started"):
        st.session_state.page = 'analyzer'
        st.rerun()
        
    st.markdown('<div class="footer">MEDCARE LABS</div>', unsafe_allow_html=True)

# ANALYZER PAGE
elif st.session_state.page == 'analyzer':
    if st.button("← Back to Home"):
        st.session_state.page = 'landing'
        st.rerun()

    st.write("### 📋 Hospital Information")
    col1, col2, col3 = st.columns(3)
    Hospital_Name = col1.text_input("Hospital Name")
    Manager_Name = col2.text_input("Manager Name")
    Branch_Office = col3.text_input("Branch")

    st.write("### ⚙️ Machine Data")
    machine1 = st.text_input("Machine 1")
    downtime1 = st.number_input("Downtime Hours 1", min_value=0.0, step=0.25, key="d1")
    machine2 = st.text_input("Machine 2")
    downtime2 = st.number_input("Downtime Hours 2", min_value=0.0, step=0.25, key="d2")
    machine3 = st.text_input("Machine 3")
    downtime3 = st.number_input("Downtime Hours 3", min_value=0.0, step=0.25, key="d3")

    if st.button("📊 Calculate & Generate Report"):
        total_downtime = downtime1 + downtime2 + downtime3
        st.success(f"Total Downtime: {total_downtime:.2f} hours")
        st.balloons()

        df = pd.DataFrame({
            "Hospital": [Hospital_Name], 
            "Manager": [Manager_Name], 
            "Branch": [Branch_Office],
            "Machine 1": [machine1], "Downtime 1": [downtime1],
            "Machine 2": [machine2], "Downtime 2": [downtime2],
            "Machine 3": [machine3], "Downtime 3": [downtime3],
            "Total": [total_downtime], 
            "Date": [datetime.now().strftime("%Y-%m-%d")]
        })

        st.dataframe(df, use_container_width=True)
        
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
            
        st.download_button("📥 Download Excel", output.getvalue(), "report.xlsx")

    st.markdown('<div class="footer">MEDCARE LABS</div>', unsafe_allow_html=True)
