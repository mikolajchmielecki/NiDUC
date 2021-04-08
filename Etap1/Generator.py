import random  # biblioteka do losowania liczb


class Generator:
    def __init__(self, m = 0):  # konstruktor buffora
        self.signal = []
        self.m = m

    def set_m(self):  # ustawienie długości buffora
        self.m = int(input("Podaj długość bufora: "))

    def generate_signal(self):  # losowe wypełnienie buffora liczbami 0 i 1
        for i in range(self.m):
            self.signal.append(random.randint(0, 1))

    def print_signal(self):  # wypisanie buffora
        print(self.signal)
