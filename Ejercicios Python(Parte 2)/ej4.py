"""Ejercicio 4
Escribir un programa que le diga al usuario que ingrese una cadena.
El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene."""

str  = input("Escribe una cadena: ")
n = 0
for x in str:
    if x.isupper():
        n += 1

print(n)
