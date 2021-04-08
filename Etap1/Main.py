from Etap1 import *
import matplotlib.pyplot as plt
import numpy as np

"""
Oblicza liczbę przekłamanych bitów
"""
def differences_number(input: list, output: list):
    suma = 0
    for i in range(0, len(input)):
        if input[i] != output[i]:
            suma += 1
    return suma


#maksymalna długość datagramu TCP
#generator = Generator.Generator(524280)

"""
Tworzy wykres zależności liczby przekłamanych bitów od prawdopodobieństwa przekłamania
"""
def plot(bits_number):
    differences_number_list = []
    for i in np.arange(0, 1, 0.05):
        results = simulation(bits_number, i)
        differences_number_list.append(differences_number(results.generator, results.decoder))

    # tworzenie wykresu
    x = np.arange(0, 1, 0.05)
    y = differences_number_list
    fig, ax = plt.subplots()
    ax.plot(x, y, 'bo', x, y, 'k')
    ax.set(xlabel='Prawdopodobieństwo przekłamania', ylabel='Liczba przekłamanych bitów',
           title=f'Zależność liczby przekłamanych bitów od prawdopodobieństwa\nLiczba transmitowanych bitów: {bits_number}')
    plt.show()

"""
Wyświetla wyniki symulacji w konsoli
"""
def print_results(bits_number, probability):
    results = simulation(bits_number, probability)
    results.print_results()

    print(f"Liczba przekłamanych bitów: {differences_number(results.generator, results.decoder)}")

"""
Przeprowadza symulację i zwraca wyniki na poszczególnych jej etapach
"""
def simulation(bits_number, probability):
    results = Results.Results()
    generator = Generator.Generator(bits_number)
    generator.generate_signal()
    results.generator = generator.signal

    coder = Coder.Coder()
    results.coder = coder.code(results.generator)

    channel = Channel.Channel(probability)
    results.channel = channel.get_output(results.coder)

    decoder = Decoder.Decoder()
    results.decoder = decoder.decode(results.channel)
    return results

plot(1000)
print_results(1000, 0.5)


