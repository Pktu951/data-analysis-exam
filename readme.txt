README - Analiza danych wypożyczalni DVD
Opis projektu


Celem projektu jest analiza danych dotyczących wypożyczeń DVD oraz stworzenie modeli predykcyjnych,
które pozwolą przewidzieć, na ile dni klient wypożyczy DVD.
Firma wypożyczająca DVD chce w ten sposób zoptymalizować zarządzanie zapasami i lepiej dostosować swoją ofertę do potrzeb klientów.
Dane wykorzystywane w projekcie znajdują się w pliku CSV "rental_info_egz.csv" i zawierają szczegółowe informacje o wypożyczeniach.


Opis danych:

"rental_date": Data i godzina wypożyczenia DVD przez klienta.
"return_date": Data i godzina zwrotu DVD przez klienta.
"amount": Kwota zapłacona przez klienta za wypożyczenie DVD.
"rental_rate": Stawka, po której DVD jest wypożyczane.
"release_year": Rok wydania wypożyczonego filmu.
"length": Długość wypożyczonego filmu w minutach.
"replacement_cost": Koszt wymiany DVD dla firmy.
"special_features": Dodatkowe funkcje, takie jak zwiastuny czy usunięte sceny, które również znajdują się na DVD.
"NC-17", "PG", "PG-13", "R": Kolumny zmiennych zero-jedynkowych określające ocenę filmu.
Jeśli film ma daną ocenę, wartość w odpowiedniej kolumnie wynosi 1, w przeciwnym razie – 0.


Firma zwróciła się o pomoc w stworzeniu i przetestowaniu modeli regresyjnych,
które pomogą przewidzieć czas wypożyczenia DVD przez klientów.
Uzyskane modele pozwolą firmie lepiej planować dostępność filmów i unikać sytuacji,
w których klienci nie mogą wypożyczyć pożądanych tytułów.


Wymagania systemowe
Python 3.11.2
Biblioteki: sklearn, numpy, pandas, matplotlib/seaborn


Struktura plików
analiza_zysku.py – Analiza przychodów
przetworzone_kolumny.py – Przetwarzanie i transformacja danych.
dane_posprocesingowe.py – Dodatkowe operacje na danych po wstępnej analizie.
modelowanie.py – Budowanie i ocena modelu predykcyjnego.



Instrukcja uruchomienia

Uruchom plik analiza_zysku.py:
python analiza_zysku.py

Uruchom plik przetworzone_kolumny.py:
python przetworzone_kolumny.py

Uruchom plik dane_posprocesingowe.py:
python dane_posprocesingowe.py

Uruchom plik modelowanie.py:
python modelowanie.py

test