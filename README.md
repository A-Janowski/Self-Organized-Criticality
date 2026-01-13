# Self-Organized Criticality – Sandpile Model (Cellular Automata)

Projekt zaliczeniowy z przedmiotu **Systemy Złożone**  

## Opis projektu

Celem projektu jest zaprezentowanie zjawiska **samoorganizacji w stanie krytycznym (Self-Organized Criticality, SOC)** na przykładzie klasycznego **modelu stożka piasku (Sandpile Model)** zaproponowanego przez Bak, Tang i Wiesenfeld.

Model został zaimplementowany jako **dwuwymiarowy automat komórkowy**, a jego ewolucja jest wizualizowana w czasie rzeczywistym. Projekt umożliwia porównanie różnych lokalnych reguł topplingu i obserwację ich wpływu na globalną dynamikę systemu.

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
- wizualizacja statyczna stanów układu
- animacja ewolucji pojedynczego modelu
- **jednoczesna animacja kilku modeli w jednym oknie** (porównanie reguł)

---

## Struktura projektu

├── sandpile.py # główna implementacja modelu i wizualizacji

├── constants.py # definicje reguł topplingu

└── README.md

---

## Wymagania

- Python 3.9+
- numpy
- matplotlib
