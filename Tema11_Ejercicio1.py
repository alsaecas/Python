import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)')

    lista_alumnos = ["Alejandro Saez", "Luis Prieto", "Diego Lopez", "Alberto Sanchez", "Juan Diaz", "Javier Sanz",
                     "Pedro Sanchez", "Jose Vives"]
    i = 1
    for alumno in lista_alumnos:
        cursor.execute(f'INSERT INTO Alumnos VALUES({i},"{alumno.split(" ")[0]}", "{alumno.split(" ")[1]}")')
        i = i + 1

    rows = cursor.execute('SELECT * FROM Alumnos WHERE Nombre = "Juan"')
    print(rows.fetchall())

    cursor.close()
    conn.close()
