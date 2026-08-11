import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Threat Level", layout="wide")

st.title("🚨 Global Threat Level")

df = pd.read_csv(
    "data/globalterrorismdb_0718dist.csv",
    encoding="latin1",
    low_memory=False
)

country = st.selectbox(
    "Select Country",
    sorted(df["country_txt"].dropna().unique())
)

country_df = df[df["country_txt"] == country]

attacks = len(country_df)
deaths = country_df["nkill"].fillna(0).sum()
injured = country_df["nwound"].fillna(0).sum()

score = (
    attacks*0.4 +
    deaths*0.4 +
    injured*0.2
)

if score < 500:
    level = "🟢 LOW"
    color = "green"
elif score < 2000:
    level = "🟡 MEDIUM"
    color = "orange"
elif score < 7000:
    level = "🟠 HIGH"
    color = "darkorange"
else:
    level = "🔴 CRITICAL"
    color = "red"

c1,c2,c3,c4 = st.columns(4)

c1.metric("Threat Score", int(score))
c2.metric("Attacks", attacks)
c3.metric("Deaths", int(deaths))
c4.metric("Injured", int(injured))

st.markdown("---")

st.markdown(
f"""
<h2 style='color:{color};'>
Current Threat Level : {level}
</h2>
""",
unsafe_allow_html=True
)

st.progress(min(int(score/100),100))

st.markdown("---")

year_df = (
    country_df.groupby("iyear")
    .size()
    .reset_index(name="Attacks")
)

fig = px.area(
    year_df,
    x="iyear",
    y="Attacks",
    title="Threat Trend"
)

st.plotly_chart(fig,use_container_width=True)

st.markdown("## Top Terror Groups")

group_df = (
    country_df["gname"]
    .value_counts()
    .head(10)
    .reset_index()
)

group_df.columns=["Group","Attacks"]

fig2 = px.bar(
    group_df,
    x="Group",
    y="Attacks",
    color="Attacks"
)

st.plotly_chart(fig2,use_container_width=True)

st.markdown("## Attack Types")

attack_df = (
    country_df["attacktype1_txt"]
    .value_counts()
    .reset_index()
)

attack_df.columns=["Attack Type","Count"]

fig3 = px.pie(
    attack_df,
    names="Attack Type",
    values="Count"
)

st.plotly_chart(fig3,use_container_width=True)

st.markdown("## AI Threat Assessment")

if score > 7000:
    st.error("""
Critical threat detected.

• Immediate surveillance recommended.

• Increase border intelligence.

• Monitor terrorist groups continuously.
""")

elif score > 2000:
    st.warning("""
High threat detected.

• Strengthen intelligence gathering.

• Increase security operations.
""")

else:
    st.success("""
Threat currently under control.

Continue monitoring activities.
""")