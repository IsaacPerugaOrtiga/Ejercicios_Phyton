"""Ejercicio 7
Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades."""


def age_people():
    
    mylist = []
    while len(mylist) in range(10):
        age = int(input("Ingrese la edad de una persona: "))
        mylist.append(age)
    return mylist

def age_greater_twenty():
    tupla = tuple(age_people())
    cont = 0
    for i in tupla:
        if i > 20:
            cont += 1
    return "Hay " + str(cont) + " persona/s que tienen mas de 20 años."

print(age_greater_twenty())