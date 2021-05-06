import numpy as np

class Results:
    def __init__(self):
        self.generator = []
        self.coder = []
        self.channel = []
        self.decoder = []

    def print_results(self):
        print("Wygenerowany sygnał:")
        print(np.array(self.generator))

        print("Zakodowany sygnał:")
        print(np.array(self.coder))

        print("Sygnał po przejściu przez kanał transmisyjny:")
        print(np.array(self.channel))

        print("Zdekodowany sygnał:")
        print(np.array(self.decoder))