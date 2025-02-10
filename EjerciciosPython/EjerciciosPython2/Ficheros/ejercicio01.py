"""
EJERCICIO 1
---------------------------------------------------------------------------------------------------------
Utilizando el fichero notas.csv, realiza un programa en python que lea los datos de ese fichero y 
construya la siguiente estructura:

    alumnos = [ {"nombre":"Daniel", "apellidos":"Fustero López", "curso": "1A","notas":{"FH":3,"LM":4,"ISO":5,"FOL":6,"PAR":7,"SGBG":6}},
                {"nombre":"Rafaela", ... },...]

Crea un programa que muestre un menú y puedas elegir una de estas opciones:
    - Muestra el listado de los alumnos con la nota media que han sacado. Utiliza una función para 
      realizar el cálculo de la nota media.
    - Pide un curso y una asignatura y muestre una lista de los alumnos de ese curso con las notas en 
      esa asignatura.
    - Pide un curso y muestre el porcentaje de aprobados por cada asignatura.
    - Pide un curso, y crea un fichero nombredelcurso.txt con los alumnos y la nota media.
"""

import csv

def leer_fichero():
    alumnos = list()
    with open("./EjerciciosPython2/Ficheros/notas.csv", newline="", encoding="utf-8") as notasCSV:
        contenido = csv.DictReader(notasCSV)
        for row in contenido:
            if all(key in row for key in ["Nombre", "Apellidos", "Curso", "FH", "LM", "ISO", "FOL", "PAR", "SGBD"]):
                alumno = {"nombre": row["Nombre"], "apellidos": row["Apellidos"], "curso": row["Curso"],
                          "notas": {"FH": int(row["FH"]), "LM": int(row["LM"]), "ISO": int(row["ISO"]),
                                    "FOL": int(row["FOL"]), "PAR": int(row["PAR"]), "SGBD": int(row["SGBD"])}}
                alumnos.append(alumno)
            #else:
            #   print(f"Fila con datos faltantes: {row}")
    print(f"Alumnos = {alumnos}")  
    return alumnos

def nota_media(alumno):
    return sum(alumno["notas"].values()) / len(alumno["notas"])

def mostrar_alumnos(alumnos):
    for alumno in alumnos:
        print(f"{alumno["nombre"]} {alumno["apellidos"]} - {nota_media(alumno)}")

def mostrar_alumnos_asignatura(alumnos, cursoBuscado, asignaturaBuscada):
    for alumno in alumnos:
        if alumno["curso"] == cursoBuscado:
            print(f"{alumno["nombre"]} {alumno["apellidos"]} - {alumno["notas"][asignaturaBuscada]}")

def porcentaje_aprobados(alumnos, curso):
    asignaturas = ["FH", "LM", "ISO", "FOL", "PAR", "SGBD"]
    for asignatura in asignaturas:
        aprobados = 0
        total_alumnos_curso = 0
        for alumno in alumnos:
            if alumno["curso"] == curso:
                total_alumnos_curso += 1
                if alumno["notas"][asignatura] >= 5:
                    aprobados += 1
        if total_alumnos_curso > 0:
            print(f"{asignatura}: {aprobados / total_alumnos_curso * 100}%")
        else:
            print(f"{asignatura}: No hay alumnos en el curso {curso}")

def crear_fichero(alumnos, curso):
    with open(f"./EjerciciosPython2/Ficheros/{curso}.txt", "w", encoding="utf-8") as file:
        for alumno in alumnos:
            if alumno["curso"] == curso:
                file.write(f"{alumno['nombre']} {alumno['apellidos']} - {nota_media(alumno)}\n")

def menu():
    alumnos = leer_fichero()
    while True:
        print("1. Mostrar alumnos con nota media")
        print("2. Mostrar alumnos de un curso y asignatura")
        print("3. Mostrar porcentaje de aprobados por asignatura")
        print("4. Crear fichero con alumnos y nota media de un curso")
        print("5. Salir")
        opcion = input("Introduce una opción: ")
        if opcion == "1":
            mostrar_alumnos(alumnos)
        elif opcion == "2":
            curso = input("Introduce un curso: ")
            asignatura = input("Introduce una asignatura: ")
            mostrar_alumnos_asignatura(alumnos, curso, asignatura)
        elif opcion == "3":
            curso = input("Introduce un curso: ")
            porcentaje_aprobados(alumnos, curso)
        elif opcion == "4":
            curso = input("Introduce un curso: ")
            crear_fichero(alumnos, curso)
        elif opcion == "5":
            break
        else:
            print("Esa opción no está disponible, escoja una que sí lo esté.")

menu()

"""notasTxt = open("./EjerciciosPython2/Ficheros/notas.txt", "r+", encoding="utf-8")

contenido = notasTxt.read()

print(contenido)"""











