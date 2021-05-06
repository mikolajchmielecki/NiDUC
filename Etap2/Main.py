from Etap1 import  Generator
from Etap2 import Simulation
from Etap2 import BCH_Parameters as p
from Etap2 import Plot
import numpy as np
from Etap1.Comparator import differences_number





# czy wyniki mają być wyświetlane w konsoli
console_info = True

# liczba powtórzeń w celu uśrednienia wyników
repeats = 20

# zakres prawdopodobieństwa
probability_range = np.arange(0.01, 0.13, 0.01)


# pętla po kolejnych podstawach kodu BCH
for m in p.m_range:

    ber_plot = Plot.Plot(f"Wykres BER kodu BCH", m, "BER", probability_range)
    e_plot = Plot.Plot(f"Wykres E kodu BCH", m, "E", probability_range)

    # pętla po kolejnych zdolnościach korekcyjnych
    for t in p.t_list[m-3]:



        simulation = Simulation.Simulation(m, t)
        _, bits_number, data_bits_number, _ = simulation.get_parameters()

        avg_BER_list = []
        avg_E_list = []

        # petla iterująca po różnych prawdopodobieństwach przekłamania bitu
        for probability in probability_range:
            BER_list = []
            E_list = []

            if console_info:
                print("------------------------------")
                print(f"m = {m}; n = {bits_number}; k = {data_bits_number}; t = {t}; probability = {probability}\n")


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
            if console_info:
                print(f"m = {m}; n = {bits_number}; k = {data_bits_number}; t = {t}; probability = {probability}")
                print(f"BER = {avg_BER}")
                print(f"E = {avg_E}")
                print("------------------------------")

            avg_BER_list.append(avg_BER)
            avg_E_list.append(avg_E)


        # dodanie wyniku do wykresu
        description = ""
        if t == 1:
            description = "kod Hamminga"
        else:
            description = "kod BCH"
        description += f" ({bits_number},{data_bits_number})"

        ber_plot.add_plot(avg_BER_list, description)
        e_plot.add_plot(avg_E_list, description)

    ber_plot.save_plot()
    e_plot.save_plot()












