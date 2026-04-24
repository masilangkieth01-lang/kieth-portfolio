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



st.title("USER_PROFILE")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://scontent.fwnp1-1.fna.fbcdn.net/v/t39.30808-6/481156842_983512053720267_4390160816734825129_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=53a332&_nc_eui2=AeEbRzj0Lbs_j9eY20cjtDpb5kN53GbKJFjmQ3ncZsokWBuNaHiwhss1Oldkfc2zLiGiupuQMjiH0Z4vrryyVC-W&_nc_ohc=BAJsDb0r3OgQ7kNvwGTA3Pd&_nc_oc=AdrS5JYeus0w-LXqy3g1soEtjjX8eIMkrBpgpBMFTtSHP2RC4mGTr90U4s80crfFhdk&_nc_zt=23&_nc_ht=scontent.fwnp1-1.fna&_nc_gid=7Ok2-_RivN76r8ptHJkRlw&oh=00_Af2uij6ocmwUxLtWTbFgkPwTjGU2xNHCpeUz2_-FH2H_8w&oe=69EFC63E", use_container_width=True)

with col2:
    st.write("""
    I am a developer in Mandaon, Masbate, specializing in web-based applications that prioritize data integrity and user experience. I believe in clean code and high-contrast design, leveraging AI-assisted logic to create practical digital solutions for local management needs.
    """)

st.subheader("Academic Credentials")
st.write("📍 **BS Computer Science**")
st.write("Focus: Networking, and Database Management.")