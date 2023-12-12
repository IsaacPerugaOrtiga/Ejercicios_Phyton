"""2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos."""
def numMax_three(n1,n2,n3):
    if(n1 > n2):
        if(n1 > n3):
            print(str(n1))
        else:
            print(n3)
    else:
        if(n2 > n3):
            print(n2)
        else:
            print(n3)

numMax_three(1,3,2)