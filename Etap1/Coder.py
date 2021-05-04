

"""
klasa Coder dziedziczy po klasie Generator
"""
class Coder:


    """
    Potraja każdą liczbę w danych wejsciowych
    """
    def code(self, data: list):
        output = []
        for i in range(0, len(data)):
            for j in range(3):
                output.append(data[i])
        return output


