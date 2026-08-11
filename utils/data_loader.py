import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    file_path = "data/globalterrorismdb_0718dist.csv"

    df = pd.read_csv(
        file_path,
        encoding="latin1",
        low_memory=False
    )

    return df