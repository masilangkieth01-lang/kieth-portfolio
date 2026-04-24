import streamlit as st

st.markdown("""
    <style>
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

st.title("CORE_COMPETENCIES")

st.subheader("Programming Logic")
st.write("Python")
st.write("55%")
st.progress(55)
st.write("PHP / MySQL")
st.write("65%")
st.progress(65)
st.write("C++")
st.write("50%")
st.progress(50)
st.write("CSS")
st.write("64%")
st.progress(64)
st.write("---")
st.subheader("Specializations")
st.markdown("""
* **Web Systems:** QR-Based Identification & Integrated Management
* **Data Visualization:** Statistical Analysis using NumPy & Matplotlib
* **UI Design:** Glassmorphism and CSS Injection
""")