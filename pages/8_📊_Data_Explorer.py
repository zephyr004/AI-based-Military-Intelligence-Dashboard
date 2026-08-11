import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Explorer",layout="wide")

st.title("📊 Data Explorer")

df=pd.read_csv(
    "data/globalterrorismdb_0718dist.csv",
    encoding="latin1",
    low_memory=False
)

st.sidebar.header("Filters")

country=st.sidebar.multiselect(
    "Country",
    sorted(df["country_txt"].dropna().unique())
)

attack=st.sidebar.multiselect(
    "Attack Type",
    sorted(df["attacktype1_txt"].dropna().unique())
)

year=st.sidebar.slider(
    "Year",
    int(df["iyear"].min()),
    int(df["iyear"].max()),
    (
        int(df["iyear"].min()),
        int(df["iyear"].max())
    )
)

filtered=df.copy()

if country:
    filtered=filtered[
        filtered["country_txt"].isin(country)
    ]

if attack:
    filtered=filtered[
        filtered["attacktype1_txt"].isin(attack)
    ]

filtered=filtered[
    (filtered["iyear"]>=year[0])&
    (filtered["iyear"]<=year[1])
]

st.metric("Filtered Records",len(filtered))

st.dataframe(
    filtered,
    use_container_width=True
)

st.subheader("Dataset Statistics")

st.write(filtered.describe())

csv=filtered.to_csv(index=False)

st.download_button(
    "⬇ Download Filtered Dataset",
    csv,
    "filtered_dataset.csv",
    "text/csv"
)

st.subheader("Missing Values")

missing=filtered.isnull().sum()

st.bar_chart(missing[missing>0])