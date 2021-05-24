class TripleCoder:

    """
    packetLen - długość pakietu danych
    scrambled = Tree - ABCABCABC
    scrambled = False - AAABBBCCC
    packetLen - orientacyjna długość pakietu
    ostatni pakiet nie musi byc tej długości
    reszta musi
    """
    def __init__(self, packetLen, scrambled):
        self.packetLen = packetLen
        self.scrambled = scrambled
        self.info = f'Potrajanie({3*packetLen},{packetLen})'
        if scrambled:
            self.info += '[ababab]'
        else:
            self.info += '[aaabbbb]'

    def __str__(self):
        info = f'Potrajanie({3 * self.packetLen},{self.packetLen})'
        if self.scrambled:
            info += '[ababab]'
        else:
            info += '[aaabbb]'
        return info

    """
    Potraja każdą liczbę w danych wejsciowych
    """
    def code(self, msg):
        output = []
        if self.scrambled:
            for i in range(3):
                output = [*output, *msg]
        else:
            for i in range(0, len(msg)):
                for j in range(3):
                    output.append(msg[i])
        return output


    """
    Dekoduje sygnał wejściowy
    """
    def decode(self, msg):
        output = []

        if self.scrambled:
            length = int(len(msg)/3)
            for i in range(length):
                suma = msg[i] + msg[i+length] + msg[i + 2*length]
                # algorytm głosujący
                if suma < 2:
                    output.append(0)
                else:
                    output.append(1)
        else:
            # sprawdzanie kolejnych trójek
            for i in range(0, len(msg), 3):
                suma = msg[i] + msg[i + 1] + msg[i + 2]
                # algorytm głosujący
                if suma < 2:
                    output.append(0)
                else:
                    output.append(1)
        return output

