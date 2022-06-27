def main():
    f = open('test.txt', 'w')
    f.write('Escribo una linea!\n')
    f.close()

    f = open('test.txt', 'r+')
    f.write('Escribo otra linea\n')
    f.close


if __name__ == '__main__':
    main()
