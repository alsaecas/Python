import pickle
from pickle import *
class Vehiculo:
    def __init__(self, marca, color, puertas):
        self.marca = marca
        self.color = color
        self.puertas = puertas

    def __str__(self):
        return f'Coche {self.marca} color {self.color} con {self.puertas} puertas'


if __name__ == '__main__':
    tesla = Vehiculo('Tesla', 'Negro', 4)
    f = open('datos.bin', 'wb')
    pickle.dump(tesla, f)
    f.close
    print('Datos guardados!')
    print('Abrimos el archivo para leer los datos guardados...')
    f = open('datos.bin', 'rb')
    print(pickle.load(f))
