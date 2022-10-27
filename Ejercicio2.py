"""
Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?

Nombre Apellido ha sacado un Nota de nota.

Ayuda

Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]

cadena = "zeréP nauJ,01"""

def Voltear_cadena(cadena):
    cadena = "zeréP nauJ,01"
    cadena = cadena[::-1]
    return cadena

def nota_alumno():
    cadena = Voltear_cadena("zeréP nauJ,01")
    nota = cadena[:2]
    alumno = cadena[3:]
    print (("{} ha sacado un {} de nota").format(alumno, nota))

nota_alumno()


