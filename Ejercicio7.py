"""
Crea un Script llamado recorrido.py que realice las siguientes funciones:

Recorre el listado del ejemplo y realiza las siguientes operaciones: [18, 50, 210, 80, 145, 333, 70, 30]

Imprimr el número en caso de que sea múltiplo de 10 y menor que 200
Parar el programa si llega a un número mayor que 300"""

def recorrido(lista):
    for i in lista:
        if i %10 == 0 and i < 200:
            print(i)
        elif i > 300:
            break

recorrido([18, 50, 210, 80, 145, 333, 70, 30])