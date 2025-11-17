import pandas as pd
import os

os.makedirs("Data/IntermediateData", exist_ok=True)
dane = pd.read_csv("Data/InputData/rental_info_egz.csv")

dane["has_trailer"] = dane["special_features"].astype(str).str.contains("Trailer").astype(int)
dane["has_commentary"] = dane["special_features"].astype(str).str.contains("Commentary").astype(int)
dane["has_deleted_scenes"] = dane["special_features"].astype(str).str.contains("Deleted Scenes").astype(int)
dane["has_behind_the_scenes"] = dane["special_features"].astype(str).str.contains("Behind the Scenes").astype(int)

dane["rental_date"] = pd.to_datetime(dane["rental_date"], errors="coerce")
dane["return_date"] = pd.to_datetime(dane["return_date"], errors="coerce")
dane["rental_duration"] = (dane["return_date"] - dane["rental_date"]).dt.days

dane["cost_per_minute"] = dane["rental_rate"] / dane["length"]

dane.to_csv("Data/IntermediateData/przetworzone_dane.csv", index=False)
print("Poprawnie zapisano plik")

dane.head(5)
