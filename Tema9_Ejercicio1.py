if __name__ == '__main__':
    lista = input("Escribe una lista de paises separados por comas: ").split(",")
    lista = [pais.strip() for pais in lista]

    print(', '.join(sorted(list(set(lista)))))
