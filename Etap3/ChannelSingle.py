import random

class ChannelSingle:
    def __init__(self, probability):
        self.probability = probability

    def __str__(self):
        return f'Błędy pojedyncze p = {self.probability}'

    """
    Metoda mająca dany strumień bitów wejściowych przekształca je na strumień bitów wyjściowych z przekłamaniami
    """
    def go_over(self, msg):
        output = []
        for bit in msg:
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
        return abs(bit - 1)