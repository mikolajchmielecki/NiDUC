import random

"""
Symuluje powstawanie błędów grupowych
"""
class ChannelGroup:
    def __init__(self, probability):
        self.probability = probability

    def __str__(self):
        return f'Błędy grupowe p = {round(self.probability, 2)}'

    """
    Metoda mająca dany strumień bitów wejściowych przekształca je na strumień bitów wyjściowych z przekłamaniami
    Losuje pozycje startową błedy grupowego
    Oblicza liczbę bitów do przekłamania
    """
    def go_over(self, msg):
        length = len(msg)
        error_bits = int(length*self.probability)
        start = random.randint(0, length-1)
        for i in range(error_bits):
            msg[(i+start)%length] = self.get_reverse_bit(msg[(i+start)%length])
        return msg

    """
    Zmienia bit wejściowy na przeciwny
    """
    @staticmethod
    def get_reverse_bit(bit):
        return abs(bit - 1)