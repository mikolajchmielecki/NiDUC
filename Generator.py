import random


class Generator:
    buffor = []
    m = 0

    def set_m(self):
        Generator.m = int(input("Podaj długość bufora: "))

    def signal(self):
        for i in range(Generator.m):
            Generator.buffor.append(random.randint(0, 1))

    def print_signal(self):
        print(Generator.buffor)
