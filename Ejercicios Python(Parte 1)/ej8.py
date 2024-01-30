"""8 - Definir una función superposicion() que tome dos listas y
devuelva True si tienen al menos 1 miembro en común o devuelva 
False de lo contrario.Escribir la función usando el bucle for anidado."""

def superposicion(list1,list2):
    for iteml1 in list1:
        for iteml2 in list2:
            if iteml1 == iteml2:
                return True
    return False

print(superposicion([1,2,3],[4,7,2]))