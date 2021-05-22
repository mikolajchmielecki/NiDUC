class Simulation:
    def __init__(self, coder, channel):
        self.coder = coder
        self.channel = channel

    """
    Dzieli wiadomość na pakiety i przesyła przez kanał transmisyjny
    Pakiety o długości możliwości kodera
    """
    def run(self, msg):

        packetLen = self.coder.packetLen
        repeats = int(len(msg)/packetLen)+1
        output = []

        data_bits_number = len(msg)
        bits_number = 0
        error_bits = 0


        for i in range(repeats):
            packet = msg[i*packetLen:(i*packetLen+packetLen)]

            # pakiet jest pusty
            if not packet:
                break

            # kodowanie
            packet = self.coder.code(packet)
            bits_number += len(packet)

            # przejście przez kanał transmisyjny
            packet = self.channel.go_over(packet)

            # dekodowanie
            packet = self.coder.decode(packet)

            # dołączanie pakietu do wyniku
            output = [*output, *packet]

        output = output[:data_bits_number]
        # print(output)

        error_bits = Simulation.differences_number(msg, output)

        BER = error_bits/data_bits_number
        E = (data_bits_number-error_bits)/bits_number
        return self.coder, BER, E

    """
    Oblicza liczbę przekłamanych bitów
    """
    @staticmethod
    def differences_number(msg1, msg2):
        sum = 0
        for i in range(0, len(msg1)):
            if msg1[i] != msg2[i]:
                sum += 1
        return sum