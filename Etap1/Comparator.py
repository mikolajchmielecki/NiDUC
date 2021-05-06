"""
Oblicza liczbę przekłamanych bitów
"""
def differences_number(input: list, output: list):
    suma = 0
    for i in range(0, len(input)):
        if input[i] != output[i]:
            suma += 1
    return suma