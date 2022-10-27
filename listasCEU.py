"""En este ejercicio se os pide crear un fichero llamado listasCEU.py que realice las siguientes funcionnes


Define una lista que contenga al menos 4 elementos de todos los tipos de valores permitidos en Python.
Selecciona cada dos elementos (uno si otro no) desde el final de la lista.
Cambia solamente la posición del primer elemento con el último elemento de la lista.
Elimina el último elemento de la lista modificada en el paso anterior.
Crea una nueva lista con la repetición de los elemento de la lista guardada en el paso anterior."""

lista = ["string", 1, True, 1.5]

lista[::-1][1::2]

def switch_primero_ultimo(lista):
    tamaño=len(lista)
    lista.append(lista[0])
    lista.insert(0, lista[tamaño-1])
    lista.pop(1)
    lista.pop(tamaño-1)
    return lista

def eliminar_ultimo(lista):
    tamaño = len(lista)
    lista = switch_primero_ultimo(lista)
    lista.pop(tamaño-1)
    return lista

nuevalista=eliminar_ultimo(lista)

print(nuevalista)