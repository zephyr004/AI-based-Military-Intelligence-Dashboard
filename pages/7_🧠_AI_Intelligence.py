import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Intelligence", layout="wide")

st.title("🧠 AI Military Intelligence")

df = pd.read_csv(
    "data/globalterrorismdb_0718dist.csv",
    encoding="latin1",
    low_memory=False
)

st.subheader("AI Intelligence Summary")

col1,col2=st.columns(2)

with col1:

    st.metric("Countries",df["country_txt"].nunique())
    st.metric("Groups",df["gname"].nunique())
    st.metric("Attack Types",df["attacktype1_txt"].nunique())

with col2:

    st.metric("Deaths",int(df["nkill"].fillna(0).sum()))
    st.metric("Injured",int(df["nwound"].fillna(0).sum()))
    st.metric("Targets",df["targtype1_txt"].nunique())

st.markdown("---")

st.subheader("Top Dangerous Countries")

country=df["country_txt"].value_counts().head(10)

st.bar_chart(country)

st.subheader("Top Terror Groups")

groups=df["gname"].value_counts().head(10)

st.bar_chart(groups)

st.subheader("Most Common Attack Types")

attack=df["attacktype1_txt"].value_counts()

st.bar_chart(attack)

st.subheader("AI Generated Intelligence")

top_country=df["country_txt"].value_counts().idxmax()
top_group=df["gname"].value_counts().idxmax()
top_attack=df["attacktype1_txt"].value_counts().idxmax()

st.info(f"""

### Executive Intelligence Brief

• Highest Activity Country : **{top_country}**

• Most Active Terror Group : **{top_group}**

• Most Common Attack Type : **{top_attack}**

### Recommendations

• Increase surveillance in high-risk regions.

• Improve border monitoring.

• Strengthen intelligence sharing.

• Monitor emerging extremist organizations.

""")

st.download_button(
    "Download Intelligence Report",
    data=df.head(100).to_csv(index=False),
    file_name="intelligence_report.csv",
    mime="text/csv"
)