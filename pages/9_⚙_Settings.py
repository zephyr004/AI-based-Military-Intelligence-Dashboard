import streamlit as st
import pandas as pd
import os
import platform
import datetime

st.set_page_config(
    page_title="Settings",
    layout="wide"
)

st.title("⚙ Settings")

st.markdown("## Dashboard Information")

df = pd.read_csv(
    "data/globalterrorismdb_0718dist.csv",
    encoding="latin1",
    low_memory=False
)

col1, col2 = st.columns(2)

with col1:

    st.metric("Dataset Rows", len(df))
    st.metric("Dataset Columns", len(df.columns))
    st.metric("Countries", df["country_txt"].nunique())
    st.metric("Groups", df["gname"].nunique())

with col2:

    st.metric("Python", platform.python_version())
    st.metric("Operating System", platform.system())
    st.metric("Current Year", datetime.datetime.now().year)
    st.metric("Project Version", "1.0")

st.markdown("---")

st.subheader("Theme")

theme = st.radio(
    "Dashboard Theme",
    [
        "Dark",
        "Light"
    ]
)

if theme == "Dark":
    st.success("Dark Theme Selected")

else:
    st.info("Light Theme Selected")

st.markdown("---")

st.subheader("Machine Learning Model")

if os.path.exists("models/attack_model.pkl"):

    st.success("✅ Attack Prediction Model Found")

else:

    st.error("❌ Attack Prediction Model Missing")

if os.path.exists("models/encoders.pkl"):

    st.success("✅ Encoder File Found")

else:

    st.error("❌ Encoder File Missing")

st.markdown("---")

st.subheader("Dataset Information")

st.write(df.dtypes)

st.markdown("---")

st.subheader("Project Modules")

modules = [
    "🏠 Home",
    "🌍 Global Threat Map",
    "🌍 Country Analysis",
    "🤖 Attack Prediction",
    "🚨 Threat Level",
    "📈 Forecasting",
    "🧠 AI Intelligence",
    "📊 Data Explorer",
    "⚙ Settings"
]

for module in modules:
    st.write("✅", module)

st.markdown("---")

st.subheader("About")

st.info("""
AI Military Intelligence Dashboard

Developed using

• Python

• Streamlit

• Plotly

• Scikit-Learn

• Pandas

• Global Terrorism Database (GTD)

Version : 1.0
""")