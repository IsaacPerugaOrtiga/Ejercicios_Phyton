"""Ejercicio 2
Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga."""

def mas_larga(list):
    for item in list:
        for item2 in list:
            if(len(item2) > len(item)):
                return item2
            
print(mas_larga(['holdad','buenas','tarasdpp']))