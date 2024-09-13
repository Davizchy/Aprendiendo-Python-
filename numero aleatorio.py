
# Generador de numeros aleatorios

import random
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

while True:
    try:
        a = int(input("INTRODUCE PRIMER NUMERO: "))
        clear()
        b = int(input("INTRODUCE SEGUNDO NUMERO: "))
        clear()

        # Verificamos que el segundo número sea mayor que el primero
        if b < a:
            print("El segundo número tiene que ser mayor que el primero.")
            continue  # Volver a pedir los números

        # Si no hay problemas, generamos el número aleatorio
        numero = random.randint(a, b)
        print("El número ganador es el:", numero)
        break

    except ValueError:
        print("Tiene que ser un número entero.")


