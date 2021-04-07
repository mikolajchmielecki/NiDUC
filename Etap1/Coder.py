

"""
klasa Coder dziedziczy po klasie Generator
"""
class Coder():


    """
    Potraja każdą liczbę w danych wejsciowych
    """
    def code(self, data: list):
        for i in range(0, len(data)*3, 3):
            data.insert(i + 1, data[i])
            data.insert(i + 2, data[i])
        return data


