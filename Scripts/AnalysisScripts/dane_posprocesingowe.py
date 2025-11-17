from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

os.makedirs("Data/IntermediateData", exist_ok=True)
df = pd.read_csv("Data/IntermediateData/przetworzone_dane.csv")

kolumny = ["rental_duration", "cost_per_minute", "rental_rate", "length", "replacement_cost"]
df["rental_duration_sq"] = df["rental_duration"].pow(2)
df = df.dropna()

skalowanie = StandardScaler()
df[kolumny] = skalowanie.fit_transform(df[kolumny])

print(df[kolumny].describe())

df.isnull().sum()

df.to_csv("Data/IntermediateData/przeskalowane_dane.csv", index=False)