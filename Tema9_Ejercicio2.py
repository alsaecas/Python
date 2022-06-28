import functools
if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    lista = list(filter(lambda x: x % 2 != 0, lista))
    result = functools.reduce(lambda a, b: a+b, lista)

    print(result)
