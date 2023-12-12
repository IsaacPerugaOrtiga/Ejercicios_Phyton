"""10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. 
Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******"""

def procedimiento(list):
    str = ''
    for x in list:
        str += x * '*' +'\n'
    return str

print(procedimiento([7,87,5]))