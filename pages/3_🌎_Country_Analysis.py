import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

st.set_page_config(layout="wide")

df = load_data()

st.title("🌎 Country Analysis")
st.markdown("### Analyze terrorist activity by country")

countries = sorted(df["country_txt"].dropna().unique())

selected_country = st.sidebar.selectbox(
    "Select Country",
    countries
)
country_df = df[df["country_txt"] == selected_country]

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Attacks",
    len(country_df)
)

c2.metric(
    "Killed",
    int(country_df["nkill"].fillna(0).sum())
)

c3.metric(
    "Wounded",
    int(country_df["nwound"].fillna(0).sum())
)

c4.metric(
    "Groups",
    country_df["gname"].nunique()
)

st.divider()

year_df = (
    country_df
    .groupby("iyear")
    .size()
    .reset_index(name="Attacks")
)

fig = px.line(
    year_df,
    x="iyear",
    y="Attacks",
    markers=True,
    title="Attacks Over Time"
)

st.plotly_chart(fig, use_container_width=True)

attack_df = (
    country_df["attacktype1_txt"]
    .value_counts()
    .reset_index()
)

attack_df.columns = ["Attack Type", "Count"]

fig2 = px.bar(
    attack_df,
    x="Attack Type",
    y="Count",
    color="Count",
    title="Attack Types"
)

st.plotly_chart(fig2, use_container_width=True)

target_df = (
    country_df["targtype1_txt"]
    .value_counts()
    .head(10)
    .reset_index()
)

target_df.columns = ["Target", "Count"]

fig3 = px.pie(
    target_df,
    names="Target",
    values="Count",
    title="Top Targets"
)

st.plotly_chart(fig3, use_container_width=True)

group_df = (
    country_df["gname"]
    .value_counts()
    .head(10)
    .reset_index()
)

group_df.columns = ["Group", "Attacks"]

fig4 = px.bar(
    group_df,
    x="Attacks",
    y="Group",
    orientation="h",
    color="Attacks",
    title="Top Terrorist Groups"
)

st.plotly_chart(fig4, use_container_width=True)

city_df = (
    country_df["city"]
    .value_counts()
    .head(15)
    .reset_index()
)

city_df.columns = ["City", "Attacks"]

fig5 = px.bar(
    city_df,
    x="City",
    y="Attacks",
    color="Attacks",
    title="Most Affected Cities"
)

st.plotly_chart(fig5, use_container_width=True)

st.subheader("Recent Incidents")

cols = [
    "iyear",
    "imonth",
    "iday",
    "city",
    "attacktype1_txt",
    "targtype1_txt",
    "gname",
    "nkill",
    "nwound"
]

available_cols = [c for c in cols if c in country_df.columns]

st.dataframe(
    country_df[available_cols].tail(20),
    use_container_width=True
)
