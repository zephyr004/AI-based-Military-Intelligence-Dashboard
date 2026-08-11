# 🛰️ AI Military Intelligence Dashboard

An AI-powered Military Intelligence Dashboard built using **Python, Streamlit, Machine Learning, and the Global Terrorism Database (GTD)**. The dashboard helps analyze historical terrorist attacks, visualize global threats, predict attack success, assess country-wise threat levels, and forecast future attack trends.

---

# 📌 Features

## 🏠 Home Dashboard
- Global terrorism overview
- Key Performance Indicators (KPIs)
- Dataset preview
- Quick statistics

---

## 🌍 Global Threat Map
- Interactive world map
- Attack locations visualization
- Hover information
- Geographic analysis

---

## 🌎 Country Analysis
- Country-wise attack analysis
- Yearly attack trends
- Top terrorist organizations
- Target analysis
- Most affected cities
- Recent incidents

---

## 🤖 Attack Prediction
Machine Learning based prediction using Random Forest.

Predicts attack success based on:

- Country
- Region
- Attack Type
- Target Type
- Weapon Type

Displays:

- Prediction
- Success Probability
- Failure Probability
- AI Assessment

---

## 🚨 Threat Level
Country-wise threat assessment using:

- Total attacks
- Deaths
- Injuries

Displays:

- Threat Score
- Threat Category
- Terror Groups
- Threat Trend
- AI Recommendations

---

## 📈 Forecasting
Historical attack trend analysis.

Includes:

- Historical attack trend
- Future prediction
- Linear Regression forecasting
- Historical vs Forecast comparison

---

## 🧠 AI Intelligence
Automatic intelligence summary including:

- Top dangerous countries
- Most active terrorist groups
- Most common attack types
- AI-generated recommendations

---

## 📊 Data Explorer
Interactive exploration of GTD dataset.

Features:

- Country filter
- Attack type filter
- Year filter
- Dataset statistics
- Missing value analysis
- CSV download

---

## ⚙️ Settings
System Information

Includes:

- Dataset information
- Model status
- Environment information
- Project details

---

# 📂 Project Structure

```
AI_MILITARY_INTELLIGENCE_DASHBOARD

│
├── assets/
├── data/
│   └── globalterrorismdb_0718dist.csv
│
├── models/
│   ├── attack_model.pkl
│   └── encoders.pkl
│
├── pages/
│   ├── Home.py
│   ├── Global_Threat_Map.py
│   ├── Country_Analysis.py
│   ├── Attack_Prediction.py
│   ├── Threat_Level.py
│   ├── Forecasting.py
│   ├── AI_Intelligence.py
│   ├── Data_Explorer.py
│   └── Settings.py
│
├── utils/
│   ├── data_loader.py
│   ├── helper.py
│   ├── styling.py
│
├── train_attack_model.py
├── app.py
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

**Global Terrorism Database (GTD)**

The Global Terrorism Database is one of the world's largest open-source databases of terrorist attacks.

Contains:

- 180,000+ incidents
- Worldwide coverage
- 1970–2017
- Country information
- Region information
- Casualties
- Terrorist groups
- Attack types
- Weapon types
- Target types

---

# 🤖 Machine Learning

Algorithm Used

- Random Forest Classifier

Training Features

- Country
- Region
- Attack Type
- Target Type
- Weapon Type

Prediction Target

- Attack Success

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-learn
- Joblib

---
