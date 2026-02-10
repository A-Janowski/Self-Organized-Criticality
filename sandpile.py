import constants
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

class Sandpile:
    """
    Klasyczny model stożka piasku (Bak-Tang-Wiesenfeld)
    oparty na automacie komórkowym 2D.
    """

    def __init__(self, size=50, rule="BTW"): # domyślnie reguła BTW, ale można zmienić
        self.size = size
        self.rule_name = rule
        self.rule = constants.RULES[rule]
        self.threshold = self.rule["threshold"]
        self.neighbors = self.rule["neighbors"]
        self.random_toppling = self.rule.get("random", False)

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
        Zwraca liczbę komórek, które runęły w tym kroku (aktywność).
        """
        unstable = np.argwhere(self.grid >= self.threshold)
        count = len(unstable) # Liczymy ile komórek jest niestabilnych
        
        if count == 0:
            return 0

        for x, y in unstable:
            self.grid[x, y] -= self.threshold
            
            # Logika sąsiadów (bez zmian, tylko wcięcie)
            if self.random_toppling:
                neighbors_idxs = np.random.choice(
                    len(self.neighbors),
                    size=self.threshold,
                    replace=True
                )
                for idx in neighbors_idxs:
                    dx, dy = self.neighbors[idx]
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.size and 0 <= ny < self.size:
                        self.grid[nx, ny] += 1
            else:
                for dx, dy in self.neighbors:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.size and 0 <= ny < self.size:
                        self.grid[nx, ny] += 1

        return count

    def relax(self):
        """
        Relaksuje układ i zwraca statystyki lawiny:
        (całkowita_wielkość, czas_trwania)
        """
        avalanche_size = 0
        avalanche_duration = 0
        
        while True:
            toppled_count = self.topple()
            if toppled_count == 0:
                break
            avalanche_size += toppled_count
            avalanche_duration += 1
            
        return avalanche_size, avalanche_duration

    def step(self):
        self.add_grain()
        return self.relax() # Zwracamy wynik relaksacji

    # -------------------------------
    # Wizualizacja dynamiczna pojedyńczego modelu
    # -------------------------------

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
# Wizualizacja dynamiczna wielu modeli jednocześnie
# -------------------------------

def animate_multiple(models, titles, steps=500, interval=50, grains_per_frame=5):
    """
    Animacja porównawcza kilku modeli stożka piasku.

    :param models: lista obiektów Sandpile
    :param titles: lista tytułów (np. nazw reguł)
    :param steps: liczba klatek animacji
    :param interval: opóźnienie między klatkami [ms]
    :param grains_per_frame: ile ziaren na klatkę
    """

    n = len(models)
    fig, axes = plt.subplots(1, n, figsize=(5 * n, 5))

    images = []
    for ax, model, title in zip(axes, models, titles):
        img = ax.imshow(
            model.grid,
            cmap="inferno",
            vmin=0,
            vmax=model.threshold
        )
        ax.set_title(title)
        ax.axis("off")
        images.append(img)

    fig.colorbar(images[0], ax=axes, fraction=0.02, pad=0.04, label="Liczba ziaren")

    def update(frame):
        for model in models:
            for _ in range(grains_per_frame):
                model.step()

        for img, model in zip(images, models):
            img.set_data(model.grid)

        fig.suptitle(f"Krok: {frame * grains_per_frame}")
        return images

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

if __name__ == "__main__":
    model_btw = Sandpile(size=50, rule="BTW")
    model_moore = Sandpile(size=50, rule="MOORE")
    model_stochastic = Sandpile(size=50, rule="STOCHASTIC")

    animate_multiple(
        models=[model_btw, model_moore, model_stochastic],
        titles=["BTW (von Neumann)", "Moore (8 sąsiadów)", "Stochastic"],
        steps=500,
        interval=50,
        grains_per_frame=10
    )