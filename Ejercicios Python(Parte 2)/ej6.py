"""Ejercicio 6
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla."""

def calculate_years_people():
    cont = 0
    name = ''
    year_bhirtday = 0
    age = 0
    summary_years = ''
    year = int(input('¿Que año es?'))
    while cont < 3:
        name = input('¿Cuál es tu nombre?')
        year_bhirtday = int(input('¿Cual es tu año de nacimiento?'))
        if year_bhirtday > year:
            summary_years += 'Los años de ' + name.capitalize() + ' no se pueden calcular porque su año de nacimiento aún no ha sido.\n'
        else:
            age = year - year_bhirtday
            summary_years += name.capitalize() + ' tiene '+ str(age) +' año/s en el año en curso ' + str(year) + '\n'
        cont += 1
    return summary_years

print(calculate_years_people())

