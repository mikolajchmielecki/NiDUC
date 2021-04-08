class Decoder:

    """
    Dekoduje sygnał wejściowy
    """
    def decode(self, input_bits: list):
        output = []
        # sprawdzanie kolejnych trójek
        for i in range(0, len(input_bits), 3):
            suma = input_bits[i] + input_bits[i+1] + input_bits[i+2]
            # algorytm głosujący
            if suma < 2:
                output.append(0);
            else:
                output.append(1)
        return output
