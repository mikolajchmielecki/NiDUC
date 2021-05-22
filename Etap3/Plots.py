import matplotlib.pyplot as plt
import mplcursors





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

    plt.scatter([1], [0], label='Przypadek idealny', marker='*')


    # sortowanie wyników po odległości Euklidesowej od przypadku idealnego (1,0)
    results = sorted(results, key=lambda result: ((result[1]-0)**2+(result[2]-1)**2))

    # minimalna odleglosc od przypadku idealnego
    _, min_BER, min_E = results[0]
    min_d = (min_BER-0)**2+(min_E-1)**2

    # rysowanie wyników
    for result in results:
        coder, BER, E = result
        d = (BER-0)**2+(E-1)**2

        if d - min_d > 0.05:
            plt.scatter([E], [BER], label=str(coder))
        else:
            plt.scatter([E], [BER], label=str(coder), marker='*')


    # wyświetlanie wykresu
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.tight_layout()

    fig = plt.gcf()
    mplcursors.cursor(hover=True)
    try:
        fig.savefig('plot.png', bbox_inches='tight')
    except Exception:
        print('[ERROR] Nie można zapisać wykresu')

    plt.show()





