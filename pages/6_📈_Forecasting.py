import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np

st.set_page_config(page_title="Forecasting", layout="wide")

st.title("📈 Terrorism Forecasting")

df = pd.read_csv(
    "data/globalterrorismdb_0718dist.csv",
    encoding="latin1",
    low_memory=False
)

year_df = (
    df.groupby("iyear")
    .size()
    .reset_index(name="Attacks")
)

st.subheader("Historical Trend")

fig = px.line(
    year_df,
    x="iyear",
    y="Attacks",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

X = year_df[["iyear"]]
y = year_df["Attacks"]

model = LinearRegression()
model.fit(X, y)

future_years = np.arange(
    year_df["iyear"].max()+1,
    year_df["iyear"].max()+11
)

future_df = pd.DataFrame({
    "iyear": future_years
})

future_df["Predicted Attacks"] = model.predict(future_df)

st.subheader("Future Forecast (Next 10 Years)")

forecast = px.line(
    future_df,
    x="iyear",
    y="Predicted Attacks",
    markers=True
)

st.plotly_chart(
    forecast,
    use_container_width=True
)

history = year_df.copy()
history.columns = ["Year","Attacks"]

future = future_df.copy()
future.columns = ["Year","Attacks"]

history["Type"] = "Historical"
future["Type"] = "Forecast"

combined = pd.concat(
    [history,future],
    ignore_index=True
)

st.subheader("Historical vs Forecast")

fig = px.line(
    combined,
    x="Year",
    y="Attacks",
    color="Type",
    markers=True
)

st.plotly_chart(fig,use_container_width=True)

growth = (
    future_df["Predicted Attacks"].iloc[-1]
    -
    future_df["Predicted Attacks"].iloc[0]
)

st.subheader("🧠 AI Forecast Summary")

if growth > 0:
    st.error(
        f"""
Forecast indicates an increase of
{int(growth)} attacks
over the next decade.

Recommendation:
Increase surveillance and
intelligence operations.
"""
    )
else:
    st.success(
        """
Forecast indicates
declining attack trend.

Recommendation:
Continue strategic monitoring.
"""
    )
st.subheader("Forecast Data")

st.dataframe(
    future_df,
    use_container_width=True
)

csv = future_df.to_csv(index=False)

st.download_button(
    "⬇ Download Forecast",
    csv,
    "forecast.csv",
    "text/csv"
)