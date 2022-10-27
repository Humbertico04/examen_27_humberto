"""
Realiza los siguientes ejercicios en un fichero llamado Ejercicio1.py:
*Convertir la variable "var_1" en todas las letras mayúsculas y en minúsculas (var_1 = "Módulo 1 de Python ")

*Consulta el tamaño o la longitud de la variable "var_1" y calcula la división de ese numero entre "7" redondeado a 4 decimales

*Realiza una función llamada funcion1  que calcule siguiente operación para que el resultado final sea igual a cero (0) //12 - (4 * 2) - (2 + 2)
*Realiza una función llamada funcion2 para que calcule la siguiente operación para que el resultado final sea igual a catorce (14)// 12 - 4 * (2 - 2) + 2
*Realiza una función llamda funcion3 para pedir al usuario que introduzca su edad, y después imprimir en la pantalla si es meyor de edad o no
Adjuntar archivo"""

import sys

var_1 = "Módulo 1 de Python "

print(var_1.upper())
print(var_1.lower())

print(round((len(var_1)/7), 4))

def funcion1():
    resultado = 12 - (4 * 2) - (2 + 2)
    print(0 == resultado)

def funcion2():
    resultado = 12 - 4 * (2 - 2) + 2
    print(14 == resultado)

def funcion3():
    while True:
        try:
            edad = int(input("Introduce tu edad: "))
        except:
            sys.stderr
        else:
            if edad<18:
                print("Eres menor de edad")
                break
            else:
                print("Eres mayor de edad")
                break

funcion1()
funcion2()
funcion3()