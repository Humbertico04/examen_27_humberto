import sys

def pedir_numero():
    while True:
        try:
            numero= int(input("Introduce un número entero: "))
        except:
            sys.stderr, print("Solo están autorizados los caracteres 0-9")
        else:
            return str(numero)

def descomposicion(numero):
    contador = 0
    while True:
        for digito in numero:
            contador+=1
            print((digito.ljust(int(contador), '0')).zfill(len(numero)), "\n")
        if contador >= len(numero):
            break

descomposicion(pedir_numero()[::-1])