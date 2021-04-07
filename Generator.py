import random  # biblioteka do losowania liczb


class Generator:
    def __init__(self):  # konstruktor buffora
        self.buffor = []
        self.m = 0

    def set_m(self):  # ustawienie długości buffora
        self.m = int(input("Podaj długość bufora: "))

    def signal(self):  # losowe wypełnienie buffora liczbami 0 i 1
        for i in range(self.m):
            self.buffor.append(random.randint(0, 1))

    def print_signal(self):  # wypisanie buffora
        print(self.buffor)
