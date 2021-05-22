from Etap3.Simulation import *

class Tests:
    def __init__(self, coders, channel):
        self.coders = coders
        self.channel = channel

    def run(self, msg):
        outputs = []
        for coder in self.coders:
            simulation = Simulation(coder, self.channel)
            outputs.append(simulation.run(msg))
            print(str(coder))

        return outputs



