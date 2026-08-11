import streamlit as st
from utils.data_loader import load_data

from utils.helper import *

df = load_data()

st.title("🏠 Home")

st.markdown("## Global Intelligence Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Attacks", format_number(total_attacks(df)))
c2.metric("Countries", format_number(total_countries(df)))
c3.metric("Groups", format_number(total_groups(df)))
c4.metric("Deaths", format_number(total_killed(df)))

st.divider()

st.subheader("Dataset Preview")

st.dataframe(df.head(20), use_container_width=True)