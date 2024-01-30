"""1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio."""

def numMax(n1,n2):
    if(n1 > n2):
        print('El número '+str(n1)+' es mayor que el número ' +str(n2)+'.')
    else:
        print('El número '+str(n2)+' es mayor que el número ' +str(n1)+'.')

numMax(4,5)