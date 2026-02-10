# Self-Organized Criticality – Sandpile Model (Cellular Automata)

Projekt zaliczeniowy z przedmiotu **Systemy Złożone**  

## Opis projektu

Celem projektu jest zaprezentowanie zjawiska **samoorganizacji w stanie krytycznym (Self-Organized Criticality, SOC)** na przykładzie klasycznego **modelu stożka piasku (Sandpile Model)** zaproponowanego przez Bak, Tang i Wiesenfeld.

Model został zaimplementowany jako **dwuwymiarowy automat komórkowy**. Projekt składa się z dwóch głównych modułów:
1.  **Wizualizacja:** Obserwacja ewolucji układu w czasie rzeczywistym i porównanie reguł.
2.  **Analiza danych:** Weryfikacja praw potęgowych (Power Laws) poprzez analizę statystyczną lawin.

---

## Zastosowane modele (reguły topplingu)

W projekcie zaimplementowano trzy warianty modelu:

### 1. BTW (Bak–Tang–Wiesenfeld)
- sąsiedztwo von Neumanna (4 sąsiadów)
- próg niestabilności: `z_c = 4`
- deterministyczna redystrybucja ziaren

### 2. Moore
- sąsiedztwo Moore’a (8 sąsiadów)
- próg niestabilności: `z_c = 8`
- deterministyczna redystrybucja ziaren

### 3. Stochastic
- sąsiedztwo von Neumanna
- próg niestabilności: `z_c = 4`
- losowy rozdział ziaren do sąsiadów

Reguły są zdefiniowane w sposób parametryczny, co umożliwia łatwe dodawanie kolejnych wariantów.

---

## Funkcjonalności

- implementacja automatu komórkowego 2D
- samoorganizacja układu do stanu krytycznego
- **wizualizacja dynamiczna:** animacja ewolucji pojedynczego modelu
- **tryb porównawczy:** jednoczesna animacja kilku modeli w jednym oknie
- **analiza statystyczna (`analysis.py`):**
    - pomiar wielkości i czasu trwania lawin
    - generowanie wykresów w skali **log-log** (weryfikacja prawa potęgowego)
    - analiza wpływu rozmiaru siatki na dynamikę (Finite Size Scaling)

---

## Struktura projektu

├── sandpile.py # główna implementacja modelu i wizualizacji

├── constants.py # definicje reguł topplingu

├── analysis.py # moduł do symulacji "headless", zbierania danych i rysowania wykresów

└── README.md

---

## Wymagania

- Python 3.9+
- numpy
- matplotlib
