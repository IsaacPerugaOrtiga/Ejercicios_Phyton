"""Ejercicio 3
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, 
y devuelva las palabras que tengan mas de n caracteres."""

def filtrar_palabras(list,n):
    str = ''
    for item in list:
        if len(item) >= n: 
            str += item + '\n'
    return str

        

print(filtrar_palabras(['lojkiljhgg','hola','buenas','sol'],7))