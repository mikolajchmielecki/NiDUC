from komm import *

"""
Klasa odpowiada za sumulacje przeprowadzaną za pomocą kodowania BCH
Z zadanymi parametrami wejściowymi oraz prawdopodobieństem przekłamania 
"""
class BCHCoder:
    def __init__(self, m, t):
        self.coder = BCHCode(m, t)
        self.m = m                              # rządz BCH
        self.n = self.coder.length              # liczba danych + dane nadmiarowe
        self.packetLen = self.coder.dimension   # liczba danych
        self.t = t                              # zdolność korekcyjna
        self.info = f'BCH({self.n},{self.packetLen})'

    def __str__(self):
        if self.t == 1:
            info = f'Hamming({self.n},{self.packetLen})'
        else:
            info = f'BCH({self.n},{self.packetLen})'
        return info

    """
    W przypadku krótszej wiadomości uzupełnienie przez 0
    """
    def code(self, msg):
        while len(msg) < self.packetLen:
            msg.append(0)
        return self.coder.encode(msg)

    def decode(self, msg):
        return self.coder.decode(msg)
