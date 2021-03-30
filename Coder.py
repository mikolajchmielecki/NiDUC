from Generator import Generator


class Coder(Generator):

    def code(self):
        for i in range(0, 3*Generator.m, 3):
            if Generator.buffor[i] == 0:
                Generator.buffor.insert(i + 1, 0)
                Generator.buffor.insert(i + 2, 0)
            else:
                Generator.buffor.insert(i + 1, 1)
                Generator.buffor.insert(i + 2, 1)


first = Coder()
first.set_m()
first.signal()
first.print_signal()
first.code()
first.print_signal()
