from Generator import Generator  # importujemy funkcje z klasy Generator


class Coder(Generator):  # klasa Coder dziedziczy po klasie Generator

    def __init__(self):  # konstruktor buffora
        super().__init__()

    def code(self):  # potrajamy każdą liczbę w bufforze
        for i in range(0, 3 * self.m, 3):
            self.buffor.insert(i + 1, self.buffor[i])
            self.buffor.insert(i + 2, self.buffor[i])


first = Coder()
first.set_m()
first.signal()
first.print_signal()
first.code()
first.print_signal()
