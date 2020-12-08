from tkinter import filedialog
from tkinter import *
from CargarArchivo import *


ir_seleccion = ArchivoCarga()


def lectura_archivo():
    print("Ingrese el Nombre del Archivo")
    nombre = input()

    direccion = nombre + ".csv"



    file = open(direccion,'r', encoding='utf-8')
    print(file)

    info = file.read()
    print (info)

def calcular_datos():
    ir_seleccion.tokens_errores()
    print("algo")



def crearJSON():
    print(algo)

def salida():
    sys.exit(0)

def opciones():
    print("\n")

    print("Seleccione una Opcion")
    print("1.Lectura de Archivo")
    print("2.Calcular Datos")
    print("3.Generar Archivo JSON")


def main_menu():
    opcion = -1
    while opcion != 4:
        opciones()
        opcion = int(input())
        if opcion == 1:
            lectura_archivo()
        elif opcion == 2:
            calcular_datos()
        elif opcion == 3:
            crearJSON()
        elif opcion == 0:
            salida()
        else:
            print("Algo")


main_menu()
"""def separador():
    print("algo") """
