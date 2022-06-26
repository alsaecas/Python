class Alumno:
    def __init__(self):
        self._nombre = None
        self._nota = None

    def inicializar(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    def imprimir(self):
        print("El alumno " + self._nombre + " tiene una nota de " + str(self._nota))

    def aprobado(self):
        if self._nota>=5:
            print("El alumno ha aprobado")
        else:
            print("El alumno ha suspendido")


alumno1 = Alumno()
alumno2 = Alumno()

alumno1.inicializar("Alejandro", 8)
alumno2.inicializar("Paco", 2)

alumno1.imprimir()
alumno2.imprimir()

alumno1.aprobado()
alumno2.aprobado()
