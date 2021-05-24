import random  # biblioteka do losowania liczb

class Generator:
    def __init__(self, m):
        self.m = m

    def generate_signal(self):  # losowe wypełnienie buffora liczbami 0 i 1
        msg = []
        for i in range(self.m):
            msg.append(random.randint(0, 1))
        return msg
