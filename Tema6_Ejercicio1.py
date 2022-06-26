class Vehiculo:
    _color = 'Blanco'
    _ruedas = 4
    _puertas = 4


class Coche(Vehiculo):
    _velocidad = 100
    _cilindrada = 500


c = Coche
print(c._velocidad)
print(c._color)
