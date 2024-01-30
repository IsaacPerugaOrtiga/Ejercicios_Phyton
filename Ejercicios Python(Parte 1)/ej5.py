"""5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24."""
def sum(list):
    num = 0
    for x in list:
        num += x
    print('La suma es igual a '+str(num))

def multp(list):
    num = 1
    for x in list:
        num *= x
    print('La multiplicación es igual a '+str(num))

sum([5,2,3])
multp([4,2,3])