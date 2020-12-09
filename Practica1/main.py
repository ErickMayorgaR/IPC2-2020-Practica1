from CalcularInfo import*


manejador = ManejaInfo()

def lectura_archivo():
    print("Ingrese la dirección del Archivo")
    direccion = input()
    
    file = open(direccion,'r', encoding='utf-8')
    #file = open("C:/Users/emayo/OneDrive/Desktop/Practica1/IPC2/Practica1/Archivo.csv", 'r', encoding='utf-8')
    datos = file.read()
    manejador.manejador(datos)


def calcular_datos():
    manejador.separarcarreras()

    print("algo")


def crearJSON():
    manejador.almacenardatosJSON()

def salida():
    exit()

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
