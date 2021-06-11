import matplotlib.pyplot as plt
import mplcursors
import numpy as np




"""
Na podstawie wyników z klasy Tests rysuje pojedynczy diagram BER od E dla danego kanału i wielu sposobów kodowania
"""
def plot_BER_E(results, channel, msg):
    plt.close()

    plt.xlim([-0.1, 1.1])
    plt.ylim([-0.1, 1.1])
    plt.title(f'Wykres BER/E dla różnych kodowań\n{str(channel)}\nLiczba bitów danych = {len(msg)}')

    plt.xlabel('E - efektywność')
    plt.ylabel('BER - stopa błędów')

    plt.scatter([1], [0], label='Przypadek idealny', marker='*', s=20)

    # wyznaczanie zbioru Pareto

    # początkowo uznajemy, że wszystkie rozwiązania są w zbiorze Pareto
    pareto = np.ones(len(results), dtype=bool)

    # algorytm przechodzi przez wszystkie rezultaty, które nie zostały jeszcze zdominowane
    # dla wybranego resultatu sprawdza czy dominuje ono pozostałe rozwiązania
    for i in range(len(results)):
        _, BER, E = results[i]
        # czy aktualny wynik jest niezdominowany
        if pareto[i]:
            # sprawdzanie zbominowania
            for j in range(len(results)):
                _, BER1, E1 = results[j]
                # sprawdzanie zdominowania
                if results[i] != results[j] and (BER1 >= BER and E1 < E) or (BER1 > BER and E1 <= E):
                    pareto[j] = False

    # rysowanie wyników
    i = 0
    for result in results:
        coder, BER, E = result

        if pareto[i]:
            plt.scatter([E], [BER], label=str(coder), marker='*', s=50)
        else:
            plt.scatter([E], [BER], label=str(coder), s=10)

        i += 1


    # wyświetlanie wykresu
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.tight_layout()
    plt.gca().invert_xaxis()
    fig = plt.gcf()
    mplcursors.cursor(hover=True)
    try:
        fig.savefig('plot.png', bbox_inches='tight', dpi=1000)
    except Exception:
        # print('[ERROR] Nie można zapisać wykresu')
        pass


    plt.show()





