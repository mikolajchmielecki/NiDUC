from komm import *
from Etap1 import Results
from Etap1 import Channel
from Etap1 import Generator

"""
Klasa odpowiada za sumulacje przeprowadzaną za pomocą kodowania BCH
Z zadanymi parametrami wejściowymi oraz prawdopodobieństem przekłamania 
"""
class Simulation:
    def __init__(self, m, t):
        self.coder = BCHCode(m, t)
        self.m = m                      # rządz BCH
        self.n = self.coder.length      # liczba danych + dane nadmiarowe
        self.k = self.coder.dimension   # liczba danych
        self.t = t                      # zdolność korekcyjna


    """
    Zwraca parametry kodu BCH
    """
    def get_parameters(self):
        return self.m, self.n, self.k, self.t

    """
    Przeprowadza symulację i zwraca wyniki na poszczególnych jej etapach
    Jako paramtery przyjmuje wiadomość wejściową oraz prawdopodobieństwo przekłamania bitu
    """
    def run(self, msg, probability):
        results = Results.Results()

        results.generator = msg

        # kodowanie sygnału
        coder_output = self.coder.encode(results.generator)
        results.coder = coder_output

        # przesyłanie sygnału przez kanał transmisyjny
        channel = Channel.Channel(probability)
        results.channel = channel.get_output(results.coder)

        decoder_output = self.coder.decode(results.channel)
        results.decoder = decoder_output
        return results


