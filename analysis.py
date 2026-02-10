import matplotlib.pyplot as plt
import numpy as np
from sandpile import Sandpile
import time

def collect_stats(size, steps=10000, rule="BTW"):
    print(f"Symulacja dla L={size}, Rule={rule}, Kroki={steps}...")
    model = Sandpile(size=size, rule=rule)
    
    # 1. Rozgrzewka (Transient) - żeby układ osiągnął stan krytyczny
    # Zazwyczaj potrzeba około size*size ziaren, dajmy bezpiecznie 2*size^2
    warmup = 2 * size * size
    for _ in range(warmup):
        model.add_grain()
        model.relax()
        
    # 2. Zbieranie danych
    sizes = []
    durations = []
    
    start_time = time.time()
    for _ in range(steps):
        s, d = model.step()
        if s > 0: # Rejestrujemy tylko jeśli wystąpiła lawina
            sizes.append(s)
            durations.append(d)
            
    print(f"-> Zakończono w {time.time()-start_time:.2f}s. Znaleziono {len(sizes)} lawin.")
    return sizes, durations

def plot_power_laws(data_dict, metric_name="Wielkość lawiny (s)"):
    """
    Rysuje wykres log-log rozkładu prawdopodobieństwa.
    data_dict: słownik {L: lista_danych}
    """
    plt.figure(figsize=(10, 6))
    
    for size, data in data_dict.items():
        data = np.array(data)
        # Obliczamy histogram (częstość występowania)
        # Logarytmiczne binowanie wygląda lepiej na wykresach SOC
        bins = np.logspace(0, np.log10(max(data)), 50)
        
        hist, bin_edges = np.histogram(data, bins=bins, density=True)
        centers = (bin_edges[:-1] + bin_edges[1:]) / 2
        
        # Filtrujemy zera (żeby log nie wybuchł)
        mask = hist > 0
        plt.loglog(centers[mask], hist[mask], '.-', label=f'L = {size}')

    plt.xlabel(f"{metric_name} (skala log)")
    plt.ylabel("Prawdopodobieństwo P(x) (skala log)")
    plt.title(f"Rozkład: {metric_name} - weryfikacja prawa potęgowego")
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.show()

if __name__ == "__main__":
    # Parametry eksperymentu
    L_values = [30, 50, 80] # Różne rozmiary siatki
    n_steps = 50000         # Ile ziaren sypiemy (im więcej tym gładszy wykres)
    
    all_sizes = {}
    all_durations = {}
    
    for L in L_values:
        # Należy zmieniać rule na BTW, MOORE lub STOCHASTIC, żeby porównać różne reguły topplingu
        s, d = collect_stats(size=L, steps=n_steps, rule="STOCHASTIC")
        all_sizes[L] = s
        all_durations[L] = d
        
    # Wykres 1: Rozkład wielkości lawin
    plot_power_laws(all_sizes, metric_name="Wielkość lawiny (liczba osunięć)")
    
    # Wykres 2: Rozkład czasu trwania lawin
    plot_power_laws(all_durations, metric_name="Czas trwania lawiny (kroki)")

    print("Gotowe! Zrzuty ekranu wykresów wklej do sprawozdania.")