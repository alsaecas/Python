if __name__ == '__main__':
    result = []
    start = int(input("Introduce numero inicial: "))
    finish = int(input("Introduce numero final: "))
    for i in range(start, finish+1):
        if i % 2 != 0:
            result.append(i)

    print(result)
