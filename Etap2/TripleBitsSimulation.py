from Etap1 import Results
from Etap1 import Generator
from Etap1 import Decoder
from Etap1 import Channel
from Etap1 import Coder

class TripleBitsSimulation:
    def __init__(self):
        self.info = "TripleBitsSimulation "

    def run(self, msg, probability):
        results = Results.Results()

        results.generator = msg

        coder = Coder.Coder()
        results.coder = coder.code(results.generator)

        channel = Channel.Channel(probability)
        results.channel = channel.get_output(results.coder)

        decoder = Decoder.Decoder()
        results.decoder = decoder.decode(results.channel)
        return results