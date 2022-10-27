"""
Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:

Borrar los elementos duplicados.
Ordenar la lista de mayor a menor.
Eliminar todos los números impares.
Realizar una suma de todos los números que quedan.
Añadir como primer elemento de la lista la suma realizada.
Devolver la lista modificada.
Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:
nueva_lista = modificar(lista)

print( nueva_lista[0] == sum(nueva_lista[1:]) )

True

Recordatorio

La función sum(lista) devuelve una suma de los elementos de una lista"""


def modificar(lista):
    nueva_lista = []
    pares = []
    for lista in lista:
        if lista not in nueva_lista:
            nueva_lista.append(lista)

    nueva_lista.sort()

    for digito in nueva_lista:
        if int(digito) % 2 == 0:
            pares.append(digito)

    pares.insert(0, sum(pares))

    print(pares[0]==sum(pares[1:]))
    print(pares)

modificar([9,8,7,6,5,2])