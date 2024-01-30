"""Ejercicio 9
Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene 
y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra."""

def cont_vocales():
    contA = 0
    contE = 0
    contI = 0 
    contO = 0
    contU = 0

    word = input("Introduce la palabra que quieras: ").upper()
    for i in word:
        if i == "A":
            contA += 1
        elif i == "E":
            contE += 1
        elif i == "I":
            contI += 1
        elif i == "O":
            contO += 1
        elif i == "U":
            contU += 1
    print("***VOCALES***")
    print("Numeros de \'A\': " + str(contA) +"\n"
          "Numeros de \'E\': " + str(contE) +"\n"
          "Numeros de \'I\': " + str(contI) +"\n"
          "Numeros de \'O\': " + str(contO) +"\n"
          "Numeros de \'U\': " + str(contU) +"\n")
        
print(cont_vocales())