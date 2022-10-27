"""
Realiza un programa llamado multiplicador.py que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

Guarda en una variable numero_magico el valor 12345679 (sin el 8)
Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
Multiplica el numero_usuario por 9 en sí mismo
Multiplica el numero_magico por el numero_usuario en sí mismo
Finalmente muestra el valor final del numero_magico por pantalla"""

import sys

numero_magico = 12345679

def pedir_numero_acotado(min, max):
    while True:
        try:
            numero_usuario = int(input("Introduce un número entre el 1 y el 9: "))
        except:
            sys.stderr
        else:
            if min < numero_usuario < max:
                return numero_usuario

numero_magico *= 9 * pedir_numero_acotado(0, 10)
 
print("El numero magico 12345679 se transformó en", numero_magico)