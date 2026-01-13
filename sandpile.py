import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

class Sandpile:
    """
    Klasyczny model stożka piasku (Bak-Tang-Wiesenfeld)
    oparty na automacie komórkowym 2D.
    """

    def __init__(self, size=50, threshold=4):
        """
        :param size: rozmiar siatki NxN
        :param threshold: próg niestabilności (z_c)
        """
        self.size = size
        self.threshold = threshold
        self.grid = np.zeros((size, size), dtype=int)

    def add_grain(self, x=None, y=None):
        """
        Dodaje jedno ziarno do losowej komórki
        lub do wskazanej pozycji.
        """
        if x is None or y is None:
            x = np.random.randint(0, self.size)
            y = np.random.randint(0, self.size)

        self.grid[x, y] += 1

    def topple(self):
        """
        Wykonuje pojedynczy krok relaksacji:
        rozładowuje wszystkie niestabilne komórki.
        Zwraca True, jeśli nastąpiło toppling.
        """
        unstable = np.argwhere(self.grid >= self.threshold)
        if len(unstable) == 0:
            return False

        for x, y in unstable:
            self.grid[x, y] -= self.threshold

            # sąsiedzi von Neumanna (góra, dół, lewo, prawo)
            if x > 0:
                self.grid[x - 1, y] += 1
            if x < self.size - 1:
                self.grid[x + 1, y] += 1
            if y > 0:
                self.grid[x, y - 1] += 1
            if y < self.size - 1:
                self.grid[x, y + 1] += 1

        return True

    def relax(self):
        """
        Relaksuje układ do stanu stabilnego.
        """
        while self.topple():
            pass

    def step(self):
        """
        Jedna iteracja modelu:
        - dodanie ziarna
        - pełna relaksacja
        """
        self.add_grain()
        self.relax()

    def animate(self, steps=5000, interval=50, grains_per_frame=5):
        """
        Animacja ewolucji stożka piasku.

        :param model: obiekt klasy Sandpile
        :param steps: liczba klatek animacji
        :param interval: opóźnienie między klatkami [ms]
        :param grains_per_frame: ile ziaren dodać na jedną klatkę
        """

        fig, ax = plt.subplots(figsize=(6, 6))
        img = ax.imshow(self.grid, cmap="inferno", vmin=0, vmax=self.threshold)
        ax.set_title("Ewolucja stożka piasku (SOC)")
        ax.axis("off")
        plt.colorbar(img, ax=ax, label="Liczba ziaren")

        def update(frame):
            for _ in range(grains_per_frame):
                self.step()

            img.set_data(self.grid)
            ax.set_title(f"Krok: {frame * grains_per_frame}")
            return [img]

        anim = animation.FuncAnimation(
            fig,
            update,
            frames=steps,
            interval=interval,
            blit=False
        )

        plt.show()



# -------------------------------
# Wizualizacja statyczna
# -------------------------------

def plot_grid(grid, title="Sandpile"):
    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap="inferno")
    plt.colorbar(label="Liczba ziaren")
    plt.title(title)
    plt.axis("off")
    plt.show()


# -------------------------------
# Przykładowe uruchomienie
# -------------------------------

if __name__ == "__main__":
    model = Sandpile(size=50, threshold=4)

    model.animate(
        steps=1000,
        interval=50,
        grains_per_frame=10
    )
