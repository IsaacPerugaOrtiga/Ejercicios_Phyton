"""3 - Definir una función que calcule la longitud de una lista o una cadena dada. 
(Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio."""
def longStr(str):
    count = 0
    for n in str:
        count += 1
        
    print(count)

longStr('nuemaasda')