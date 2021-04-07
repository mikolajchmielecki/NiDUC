import random

"""
Klasa implementuje zachoweanie fizycznego kanału transmisyjnego
"""
class Channel:
    """
    Konstruktor klasy Channel
    Podaje się prawdopodobieństwo z jakim dany bit może zostać przekłamany
    """
    def __init__(self, probability):
        self.probability = probability

    """
    Metoda mająca dany strumień bitów wejściowych przekształca je na strumień bitów wyjściowych z przekłamaniami
    """
    def get_output(self, input_bits):
        output = []
        for bit in input_bits:
            temp = bit
            if random.random() < self.probability:
                temp = self.get_reverse_bit(bit)
            output.append(temp)

        return output

    """
    Zmienia bit wejściowy na przeciwny
    """
    @staticmethod
    def get_reverse_bit(bit):
        return abs(bit-1)
