import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Attack Prediction", layout="wide")

st.title("🤖 AI Attack Prediction")
st.markdown("### Predict Probability of Terrorist Attack Success")

model = joblib.load("models/attack_model.pkl")
encoders = joblib.load("models/encoders.pkl")

df = pd.read_csv(
    "data/globalterrorismdb_0718dist.csv",
    encoding="latin1",
    low_memory=False
)

col1, col2 = st.columns(2)

with col1:
    country = st.selectbox(
        "Country",
        sorted(df["country_txt"].dropna().unique())
    )

    region = st.selectbox(
        "Region",
        sorted(df["region_txt"].dropna().unique())
    )

    attack = st.selectbox(
        "Attack Type",
        sorted(df["attacktype1_txt"].dropna().unique())
    )

with col2:
    target = st.selectbox(
        "Target Type",
        sorted(df["targtype1_txt"].dropna().unique())
    )

    weapon = st.selectbox(
        "Weapon Type",
        sorted(df["weaptype1_txt"].dropna().unique())
    )


if st.button("🚀 Predict"):

    X = pd.DataFrame({
        "country_txt":[encoders["country_txt"].transform([country])[0]],
        "region_txt":[encoders["region_txt"].transform([region])[0]],
        "attacktype1_txt":[encoders["attacktype1_txt"].transform([attack])[0]],
        "targtype1_txt":[encoders["targtype1_txt"].transform([target])[0]],
        "weaptype1_txt":[encoders["weaptype1_txt"].transform([weapon])[0]]
    })

    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0]

    success = probability[1] * 100
    failure = probability[0] * 100

    st.divider()

    if prediction == 1:
        st.success("✅ High Probability of Successful Attack")
    else:
        st.error("❌ Low Probability of Successful Attack")

    st.metric(
        "Success Probability",
        f"{success:.2f}%"
    )

    st.progress(int(success))

    st.metric(
        "Failure Probability",
        f"{failure:.2f}%"
    )

    st.bar_chart(
        pd.DataFrame({
            "Probability":[success, failure]
        }, index=["Success","Failure"])
    )

    st.info(f""""
### AI Military Assessment

• Country : **{country}**

• Region : **{region}**

• Attack Type : **{attack}**

• Target : **{target}**

• Weapon : **{weapon}**

The prediction is generated using a Random Forest model trained on the Global Terrorism Database.
""")