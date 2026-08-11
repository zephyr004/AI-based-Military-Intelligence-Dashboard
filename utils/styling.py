import streamlit as st

def load_css():

    st.markdown(
        """
        <style>

        .main{
            background-color:#0E1117;
        }

        h1,h2,h3,h4{
            color:white;
        }

        .stMetric{
            background:#1f2937;
            padding:15px;
            border-radius:12px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )