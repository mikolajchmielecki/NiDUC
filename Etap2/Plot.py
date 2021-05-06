import matplotlib.pyplot as plt
import numpy as np
"""
Rysowanie wykresów różnych statystyk
"""
class Plot:
    plot_number = 0

    """
    Tworzy wykres o danej skali x oraz tytułach osi
    """
    def __init__(self, title, subtitle, statistics, probability_range):
        self.number = Plot.plot_number
        Plot.plot_number += 1

        self.subtitle = subtitle
        self.statistics = statistics
        plt.figure(self.number)
        plt.tight_layout()
        plt.title(title + subtitle)
        plt.xlabel("Prawdopodobieństwo przekłamania bitu")
        plt.ylabel(f"Współczynnik {statistics}")
        self.probabilities = list(probability_range)


    def add_plot(self, y, description):
        plt.figure(self.number)
        plt.plot(self.probabilities, y, label=description, marker='o')

    def save_plot(self):
        fig = plt.figure(self.number)
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

        m = 0
        if len(self.subtitle) > 0:
            m = self.subtitle[-1]

        path = ''
        # porównanie z potrajaniem
        if m == 0:
            path = 'wykresy/' + self.statistics + '_BCH_vs_potrajanie.png'
        else:
            path = 'wykresy/' + self.statistics + f'_{m}.png'

        fig.savefig(path, bbox_inches='tight')
        plt.close()

