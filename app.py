import streamlit as st

st.set_page_config(
    page_title="System Architect | Portfolio",
    page_icon="🌌",
    layout="wide"
)

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #00f2ff;
    }
    
    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(0, 242, 255, 0.2);
    }

    h1 {
        color: #00f2ff !important;
        text-shadow: 0 0 10px #00f2ff, 0 0 20px #00f2ff;
        font-family: 'Courier New', Courier, monospace;
    }

    .stButton>button {
        background-color: transparent;
        color: #00f2ff;
        border: 1px solid #00f2ff;
        border-radius: 5px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00f2ff;
        color: #000;
        box-shadow: 0 0 15px #00f2ff;
    }
    </style>
  """, unsafe_allow_html=True)

st.title("WELCOME TO MY PORTFOLIO")
st.write("---")
st.markdown("""
I am a developer focused on systematic efficiency and modern design architecture.
Use the navigation on the left to initialize specific modules.
""")
st.page_link("pages/1_Home.py", label="Let's Start")
st.markdown("<br><br>", unsafe_allow_html=True)
st.info("System Ready. Click above to begin the data transmission.")
