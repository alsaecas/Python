import math


def area_triangulo(base, altura):
    return base * altura / 2


def area_circulo(radio):
    return math.pi * radio ** 2


if __name__ == '__main__':
    base = float(input("Introduce la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    print("El área del triángulo es:" + str(area_triangulo(base, altura)))
    radio = float(input("Introduce el radio del círculo: "))
    print("El área del círculo es:" + str(area_circulo(radio)))
