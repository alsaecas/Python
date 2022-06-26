class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self._color = color
        self._ruedas = ruedas
        self._puertas = puertas


class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self._velocidad = velocidad
        self._cilindrada = cilindrada

    def __str__(self):
        return "Color: " + self._color + ", ruedas: " + str(self._ruedas) + ", puertas: " + str(
            self._puertas) + ", velocidad: " + str(self._velocidad) + ", cilindrada: " + str(self._cilindrada)


c = Coche("Blanco", 4, 4, 100, 500)
print(c)
