"""Ejercicio 2
Escribe un programa que te permita jugar a una versión simplificada del
juego Master Mind. El juego consistirá en adivinar una cadena de números
distintos. Al principio, el programa debe pedir la longitud de la cadena (de 2
a 9 cifras). Después el programa debe ir pidiendo que intentes adivinar la
cadena de números. En cada intento, el programa informará de cuántos números
han sido acertados (el programa considerará que se ha acertado un número si
coincide el valor y la posición)."""
import random

def numbersMasterMindGame():
    number = int(input("Dame un numero del 2 al 9: "))
    n = ""
    if number >= 2 or number <= 9:
        for it in range(number):
            it = random.randint(0,9)
            n += str(it)
    else:
       print("El siguiente numero no esta en el rango de 2 a 9.") 

print(numbersMasterMindGame())