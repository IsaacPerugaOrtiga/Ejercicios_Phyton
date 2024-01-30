"""4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False."""
def isVocal(n):
    if(n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u'):
        return True
    elif(n == 'A' or n == 'E' or n == 'I' or n == 'O' or n == 'U'):
        return True
    else:
        return False 
        
isVocal('J')
