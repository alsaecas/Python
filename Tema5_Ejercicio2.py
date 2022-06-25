import math


def es_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    numero = int(input("Introduce un número: "))
    print(es_primo(numero))
