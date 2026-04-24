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

st.header("Greetings, I'm Kieth")
st.subheader("| Full-Stack Developer")

st.image("https://scontent.fmnl25-4.fna.fbcdn.net/v/t39.30808-6/480570386_977496224321850_3556259836291161587_n.jpg?stp=c0.17.768.768a_dst-jpg_s206x206_tt6&_nc_cat=107&ccb=1-7&_nc_sid=3da8dc&_nc_eui2=AeH0L32dL7T6glgM1NA4gzpRiFgdHYwMH1aIWB0djAwfViwiQ_s7YloB6vyiHfXbEX63pAKTEJI4zT3IoEsfKCFu&_nc_ohc=htPkIQgyvqQQ7kNvwFdQpKz&_nc_oc=AdqAw7cIfOBDaTnRrCw_YqV5pw_f6ItgraDzbTnsokwXDAK9_nfWOmeJY231dIBBNA4&_nc_zt=23&_nc_ht=scontent.fmnl25-4.fna&_nc_gid=4Nkl8FCstRYb3OLE-JnXEQ&oh=00_Af3gF6O5X6aeqKfHm_R981GlKCzVYGUMcNzi44CdiT8NwQ&oe=69EFFBD2", 
         caption="Decoding the Future")

st.info("Currently specializing in Integrated Management Systems and Automated Logic.")


st.markdown('<p class="neon-text">WELCOME TO MY PORTFOLIO</p>', unsafe_allow_html=True)
st.write("---")
st.write("I am a developer focused on systematic efficiency and modern design architecture.")