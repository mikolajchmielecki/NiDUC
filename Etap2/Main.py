from Etap1 import  Generator
from Etap2 import BCH_Simulation
from Etap2 import BCH_Parameters as p
from Etap2 import TripleBitsSimulation
from Etap2 import Plot
import numpy as np
from Etap1.Comparator import differences_number


def repeat_simulation(probability_range, repeats, simulation, console_info):
    avg_BER_list = []
    avg_E_list = []
    # petla iterująca po różnych prawdopodobieństwach przekłamania bitu
    for probability in probability_range:
        BER_list = []
        E_list = []
        print("------------------------------")
        print(simulation.info + f" probability = {probability}")

        for i in range(repeats):
            # generowanie losowego sygnału
            generator = Generator.Generator(data_bits_number)
            generator.generate_signal()

            # uruchamianie symulacji
            results = simulation.run(generator.signal, probability)

            distort_bits = differences_number(results.generator, results.decoder)

            # statystyki
            BER = distort_bits / data_bits_number
            BER_list.append(BER)
            E = (data_bits_number - distort_bits) / bits_number
            E_list.append(E)

            if console_info:
                results.print_results()
                print(f"Przekłamane bity: {distort_bits}")
                print(f"BER = {BER}; E = {E}")
                print()
        avg_BER = sum(BER_list) / len(BER_list)
        avg_E = sum(E_list) / len(E_list)

        print(f"BER = {avg_BER}")
        print(f"E = {avg_E}")
        avg_BER_list.append(avg_BER)
        avg_E_list.append(avg_E)

    return avg_BER_list, avg_E_list

# czy wyniki mają być wyświetlane w konsoli
console_info = False

# liczba powtórzeń w celu uśrednienia wyników
repeats = 20

# zakres prawdopodobieństwa
probability_range = np.arange(0.01, 0.16, 0.01)



# porównanie BCH i potrajania
m = 6
t = 7
ber_plot = Plot.Plot(f"Wykres BER - porównanie kodu BCH i potrajania", '', "BER", probability_range)
e_plot = Plot.Plot(f"Wykres E - porównanie kodu BCH i potrajania", '', "E", probability_range)


simulation = BCH_Simulation.BCH_Simulation(m, t)
_, bits_number, data_bits_number, _ = simulation.get_parameters()
avg_BER_list, avg_E_list = repeat_simulation(probability_range, repeats, simulation, console_info)
ber_plot.add_plot(avg_BER_list, f"BCH({bits_number}, {data_bits_number})")
e_plot.add_plot(avg_E_list, f"BCH({bits_number}, {data_bits_number})")

simulation1 = TripleBitsSimulation.TripleBitsSimulation()
avg_BER_list, avg_E_list = repeat_simulation(probability_range, repeats, simulation1, console_info)
ber_plot.add_plot(avg_BER_list, f"potrajanie({bits_number}, {round(bits_number/3)})")
e_plot.add_plot(avg_E_list, f"potrajanie({bits_number}, {round(bits_number/3)})")

ber_plot.save_plot()
e_plot.save_plot()


# pętla po kolejnych podstawach kodu BCH
for m in p.m_range:

    ber_plot = Plot.Plot(f"Wykres BER kodu BCH", f"\nm = {m}", "BER", probability_range)
    e_plot = Plot.Plot(f"Wykres E kodu BCH", f"\nm = {m}", "E", probability_range)

    # pętla po kolejnych zdolnościach korekcyjnych
    for t in p.t_list[m-3]:
        simulation = BCH_Simulation.BCH_Simulation(m, t)
        _, bits_number, data_bits_number, _ = simulation.get_parameters()

        avg_BER_list, avg_E_list = repeat_simulation(probability_range, repeats, simulation, console_info)

        # dodanie wyniku do wykresu
        description = ""
        if t == 1:
            description = "Hamming"
        else:
            description = "BCH"
        description += f" ({bits_number},{data_bits_number})"

        ber_plot.add_plot(avg_BER_list, description)
        e_plot.add_plot(avg_E_list, description)

        print("******************************")

    ber_plot.save_plot()
    e_plot.save_plot()












