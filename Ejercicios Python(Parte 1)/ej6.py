"""6 - Definir una función inversa() que calcule la inversión de una cadena.
 Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"""

def inversa(str):
    str2 = ''
    for x in str:
        str2 = x + str2
    return str2

print(inversa('hola'))
