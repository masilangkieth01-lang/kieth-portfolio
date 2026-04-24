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

st.markdown('<p class="neon-text"> CONTACT ME</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("Connect with Me!")
    st.write("For collaborations, inquiries, or technical support regarding my systems.")
    
    # Professional Links
    st.markdown("""
    - 📧 **Email:** .masilangkieth01@gmail.com
    - 🐙 **GitHub:** https://github.com/masilangkieth01-lang
    - 📍 **Location:** Mandaon, Masbate, PH
    """)

with col2:
    with st.form("contact_form"):
        st.write("### Send a Message")
        name = st.text_input("Name", placeholder="Enter your name")
        email = st.text_input("Email", placeholder="yourname@domain.com")
        subject = st.selectbox("Subject", ["General Inquiry", "Project Collaboration", "Bug Report", "Other"])
        message = st.text_area("Message", placeholder="Type your message here...")
        
        submit = st.form_submit_button("SEND")
        if submit:
            st.success("Message sent!")