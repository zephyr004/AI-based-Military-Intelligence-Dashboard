import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(
    "data/globalterrorismdb_0718dist.csv",
    encoding="latin1",
    low_memory=False
)

columns = [
    "country_txt",
    "region_txt",
    "attacktype1_txt",
    "targtype1_txt",
    "weaptype1_txt",
    "success"
]

df = df[columns].dropna()

encoders = {}

for col in columns[:-1]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

X = df.drop("success", axis=1)
y = df["success"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model, "models/attack_model.pkl")
joblib.dump(encoders, "models/encoders.pkl")

print("Model Saved Successfully")