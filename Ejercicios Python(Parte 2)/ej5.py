"""Ejercicio 5
Construir un pequeño programa que convierta números binarios en enteros.""" 

def reversed_num(num):
    str = ''
    for x in num:
        str = x + str
    return str

def converter(num):
    sum = 0
    n = 0
    digit = 0
    str = reversed_num(num)
    for x in str:
        n = int(x)
        str = ''
        sum += int(n * 2 ** digit) 
        digit += 1
    return sum


print(converter('010'))

