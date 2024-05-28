"""Ejercicio 3
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden
las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
últimas tiene que decir que riman un poco y si no, que no riman."""

def isRhyme():
    str = input("Dime la primera palabra: ")
    str2 = input("Dime la segunda palabra: ")
    if(str[-3:] == str2[-3:]):
        print("Estas palabras riman")
    elif(str[-2:] == str2[-2:]):
        print("Estas palabras riman un poco")
    else:
        print("Estas palabras no riman")

isRhyme()
