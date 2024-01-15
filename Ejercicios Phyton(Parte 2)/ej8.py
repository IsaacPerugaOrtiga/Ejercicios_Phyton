"""Ejercicio 8
Definir una lista con un conjunto de nombres, imprimir la cantidad que comienzan con la letra a.
También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)"""

def search_people_first_word():
    mylist = ['Juan','Alberto','Aarón','Sandro','José']
    cont = 0
    word = input('Porque letra quieres que se encuentren nombres que empiezan por esta misma: ').upper()
    for i in mylist:
        if i[0] == word:
            cont += 1
    return cont

print(search_people_first_word())