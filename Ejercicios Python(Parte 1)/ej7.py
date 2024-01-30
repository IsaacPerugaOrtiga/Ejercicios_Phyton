"""7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, 
palabras que tienen el mismo aspecto escritas invertidas),
 ejemplo: es_palindromo ("radar") tendría que devolver True."""

def es_palindromo(str):
    str2 = ''
    for x in str:
        str2 = x +str2
    if str == str2:
        return True
    return False

print(es_palindromo('lal'))