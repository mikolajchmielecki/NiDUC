class Results:
    def __init__(self):
        self.generator = []
        self.coder = []
        self.channel = []
        self.decoder = []

    def print_results(self):

        print("Wygenerowany sygnał:")
        print(self.generator)

        print("Zakodowany sygnał:")
        print(self.coder)

        print("Sygnał po przejściu przez kanał transmisyjny:")
        print(self.channel)

        print("Zdekodowany sygnał:")
        print(self.decoder)