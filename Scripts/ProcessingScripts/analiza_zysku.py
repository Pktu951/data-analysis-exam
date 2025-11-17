import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("Output/Results", exist_ok=True)
dane = pd.read_csv("Data/InputData/rental_info_egz.csv").dropna()
usuniete = len(dane)

dane = dane.dropna()
print(f'Usunięto {usuniete - len(dane)} wierszy')

dane.to_csv("Data/IntermediateData/wyczyszczone_dane.csv", index=False)

dochod_roczny = dane.groupby("release_year")["amount"].sum().sort_values(ascending=False)
najlepsze_lata = [2004, 2006, 2007]

dochod_roczny.to_csv("Data/IntermediateData/dochod_roczny.csv")

plt.figure(figsize=(10, 5))
plt.bar(dochod_roczny.index, dochod_roczny.values, color='#4682B4', label="Pozostałe lata")
plt.bar(najlepsze_lata, dochod_roczny.loc[najlepsze_lata], color='#FF4500', label="Top 3 lata")
plt.xlabel("Rok wydania")
plt.ylabel("Dochód")
plt.title("Dochód według roku wydania")
plt.legend()
plt.savefig("Output/Results/calkowity_przychod.png")
plt.close()

for rok in najlepsze_lata:
    oceny = dane[dane["release_year"] == rok][["NC-17", "PG", "PG-13", "R"]].sum()

    plt.figure(figsize=(6, 4))
    plt.bar(oceny.index, oceny.values, color=['#1E90FF', '#32CD32', '#FF8C00', '#8A2BE2'])
    plt.xlabel("Ocena")
    plt.ylabel("Liczba filmów")
    plt.title(f"Rozkład ocen w {rok} roku")
    plt.savefig(f"Output/Results/rozklad_ocen{rok}.png")
    plt.close()

print("Zapisano wszystkie pliki")