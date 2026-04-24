import streamlit as st

st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #00f2ff;
    }

    [data-testid="stSidebar"] {
        background-color: rgba(20, 20, 40, 0.9) !important;
        border-right: 1px solid #00f2ff;
    }

    .neon-text {
        color: #00f2ff !important;
        text-shadow: 0 0 10px #00f2ff, 0 0 20px #00f2ff;
        font-family: 'Courier New', Courier, monospace;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
    }

    .block-container {
        animation: fadeIn 0.6s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)

st.title("PROJECT_REPOS")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.write("### Project T.R.A.C.E.")
        st.write("Integrated Barangay Management System with QR ID integration.")
        st.caption("Tech: PHP, MySQL, CSS")

with col2:
    with st.container(border=True):
        st.write("### BoardingHouse System")
        st.write("A reservation command center with real-time availability tracking.")
        st.caption("Tech: PHP, Web Design")

st.write("---")
with st.expander("View Data Visualization Projects"):
    st.write("Statistical distribution and sales tracking scripts built with Python.")

    # (Paste the SHARED DESIGN BLOCK here)

st.markdown('<p class="neon-text">PROJECT MODULES</p>', unsafe_allow_html=True)
st.write("---")

with st.container():
    st.write("### Project T.R.A.C.E.")
    st.write("Integrated Barangay Management System for Barangay Tumalaytay.")
    st.info("Status: Working...")