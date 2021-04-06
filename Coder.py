from Generator import Generator


class Coder(Generator):

    def code(self):
        for i in range(0, 3*Generator.m, 3):
            Generator.buffor.insert(i + 1, Generator.buffor[i])
            Generator.buffor.insert(i + 2, Generator.buffor[i])


first = Coder()
first.set_m()
first.signal()
first.print_signal()
first.code()
first.print_signal()
