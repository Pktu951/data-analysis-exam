import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor

# Wczytanie danych
data = pd.read_csv("Data/IntermediateData/przeskalowane_dane.csv")

# Definicja cech oraz zmiennej docelowej
feature_cols = ["rental_rate", "cost_per_minute", "length", "replacement_cost", "amount"]
X, y = data[feature_cols], data["rental_duration"]

# Podział danych
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=45)

# Trening modelu regresji liniowej
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred_lin = lin_reg.predict(X_test)

# Metryki regresji liniowej
metrics_lin = {
    "R^2": r2_score(y_test, y_pred_lin),
    "MSE": mean_squared_error(y_test, y_pred_lin)
}

# Wizualizacja wyników regresji liniowej
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred_lin, alpha=0.5)
plt.xlabel("Rzeczywisty czas wypożyczenia (dni)")
plt.ylabel("Przewidywany czas wypożyczenia (dni)")
plt.title(f"Regresja liniowa: rzeczywiste vs przewidywane (R² = {metrics_lin['R^2']:.3f})")
plt.axline((0, 0), slope=1, color="green", linestyle="--")
plt.savefig("Output/Results/regresja_liniowa.png")
plt.close()

# Trening modelu XGBoost
xgb_reg = XGBRegressor(objective="reg:squarederror", random_state=24)
xgb_reg.fit(X_train, y_train)
y_pred_xgb = xgb_reg.predict(X_test)

# Metryki modelu XGBoost
metrics_xgb = {
    "R^2": r2_score(y_test, y_pred_xgb),
    "MSE": mean_squared_error(y_test, y_pred_xgb)
}

# Wizualizacja wyników modelu XGBoost
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred_xgb, alpha=0.5)
plt.xlabel("Rzeczywisty czas wypożyczenia (dni)")
plt.ylabel("Prognozowany czas wypożyczenia (dni)")
plt.title(f"XGBoost Regression: rzeczywiste vs prognozowane (R² = {metrics_xgb['R^2']:.3f})")
plt.axline((0, 0), slope=1, color="green", linestyle="--", label="Idealne dopasowanie")
plt.savefig("Output/Results/xgboost_regresja.png")
plt.close()