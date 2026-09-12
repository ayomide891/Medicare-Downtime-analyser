import streamlit as st

st.set_page_config(page_title="Medicare Downtime Analyzer", page_icon="🏥", layout="wide")
st.title("🏥 MEDCARE LABS")
st.subheader("Downtime Analysis And Repair Funds Recalibration")

col1, col2 = st.columns(2)
with col1:
    Manager_Name = st.text_input("Manager Name")
with col2:
    Branch_Office = st.text_input("Branch Office")

st.divider()
st.write("### Enter Machine Data")
machine1 = st.text_input("Machine 1 Name", "Hematology")
downtime1 = st.number_input(f"{machine1} Downtime in mins", min_value=0, value=180)

machine2 = st.text_input("Machine 2 Name", "Chemistry")
downtime2 = st.number_input(f"{machine2} Downtime in mins", min_value=0, value=150)

machine3 = st.text_input("Machine 3 Name", "PCR")
downtime3 = st.number_input(f"{machine3} Downtime in mins", min_value=0, value=240)

if st.button("🚨 ANALYZE & RECOMMEND", type="primary"):
    downtimes = {machine1: downtime1, machine2: downtime2, machine3: downtime3}
    Most_important = max(downtimes, key=downtimes.get)
    Highest = downtimes[Most_important]
    
    st.success("==RESULTS==")
    st.metric("Most Important Machine to Fix", Most_important)
    st.metric("Highest Downtime", f"{Highest} mins")
    st.write(f"**Manager:** {Manager_Name} | **Branch:** {Branch_Office}")
    st.info("--WE CARE FOR YOUR HEALTH--")
