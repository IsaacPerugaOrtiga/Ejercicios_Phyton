"""Ejercicio 10
Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto.Un año bisiesto es divisible por 4, pero no por 100. Tampoco es divisible por 400"""

def es_bisiesto():
    year = int(input("¿Que año quieres comprobar que es bisiesto?"))
    if year % 4 == 0:
        if year % 100 != 0:
            if year % 400 != 0:
                return "El año "+str(year)+" es bisiesto."
            else:
                return "El año "+str(year)+" no es bisiesto. Es divisble por 400."
        else:
            return  "El año "+str(year)+" no es bisiesto.Es divisble por 100."
    else:
        return "El año "+str(year)+" no es bisiesto. No es divisble por 4."
    
print(es_bisiesto())