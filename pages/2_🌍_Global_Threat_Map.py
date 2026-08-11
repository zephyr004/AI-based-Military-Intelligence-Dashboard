import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

st.title("🌍 Global Threat Map")

df = load_data()

df = df.dropna(
    subset=["latitude","longitude"]
)

fig = px.scatter_map(
    df,
    lat="latitude",
    lon="longitude",
    hover_name="country_txt",
    hover_data=[
        "city",
        "attacktype1_txt",
        "gname"
    ],
    zoom=1,
    height=700
)

fig.update_layout(
    mapbox_style="carto-darkmatter",
    margin=dict(
        l=0,
        r=0,
        t=0,
        b=0
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)