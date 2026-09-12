import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="MEDCARE LABS - Downtime Analyzer",
    page_icon="🏥",
    layout="wide"
)

# CUSTOM CSS FOR PRO LOOK
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #1e3a8a 0%, #2563eb 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .footer {
        text-align: center;
        color: #64748b;
        padding: 1rem;
        margin-top: 3rem;
    }
    </style>
""", unsafe_allow_html=True)

# SESSION STATE TO SWITCH PAGES
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

# LANDING PAGE
if st.session_state.page == 'landing':
    st.markdown("""
        <div class="main-header">
            <h1>🏥 MEDCARE LABS</h1>
            <h3>Downtime Analysis & Repair Funds Recalibration</h3>
            <p>Track machine downtime. Calculate repair funds. For ANY hospital, ANY lab.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("https://img.icons8.com/color/96/hospital-2.png", width=100)
        st.write("")
        if st.button("🚀 Get Started", use_container_width=True, type="primary"):
            st.session_state.page = 'analyzer'
            st.rerun()
        st.write("")
        st.info("✅ Works for all hospitals, clinics, and diagnostic centers worldwide")

    st.markdown('<div class="footer">© 2026 MEDCARE LABS - Built for Healthcare Facilities</div>', unsafe_allow_html=True)

# ANALYZER PAGE
else:
    st.title("🏥 MEDCARE LABS")
    st.subheader("Downtime Analysis & Repair Funds Recalibration")
    
    if st.button("← Back to Home"):
        st.session_state.page = 'landing'
        st.rerun()
    
    st.divider()
    
    # HOSPITAL INFO - NOW FOR ANY HOSPITAL
    st.write("### 📋 Hospital Information")
    col1, col2, col3 = st.columns(3)
    with col1:
        Hospital_Name = st.text_input("Hospital Name")
    with col2:
        Manager_Name = st.text_input("Manager Name")
    with col3:
        Branch_Office = st.text_input("Branch/Department")
    
    st.divider()
    st.write("### ⚙️ Enter Machine Data")
    
    machine1 = st.text_input("Machine 1 Name", placeholder="e.g. Hematology Analyzer")
    downtime1 = st.number_input(f"Downtime Hours for {machine1}", min_value=0.0, step=0.5)
    
    machine2 = st.text_input("Machine 2 Name", placeholder="e.g. Chemistry Analyzer")
    downtime2 = st.number_input(f"Downtime Hours for {machine2}", min_value=0.0, step=0.5)
    
    machine3 = st.text_input("Machine 3 Name", placeholder="e.g. X-Ray Machine")
    downtime3 = st.number_input(f"Downtime Hours for {machine3}", min_value=0.0, step=0.5)
    
    if st.button("📊 Calculate & Generate Report", type="primary"):
        total_downtime = downtime1 + downtime2 + downtime3
        st.success(f"Total Downtime: {total_downtime} hours")
        st.balloons()
    
    st.markdown('<div class="footer">MEDCARE LABS - For all Healthcare Facilities</div>', unsafe_allow_html=True)
