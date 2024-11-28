""" Este programa muestra primero el listado de categorías de películas 
y pide al usuario que introduzca el código de la categoría de la película 
y posterior a ello pide que el usuario introduzca el número de días de atraso, 
y así se muestra al final el total a pagar."""
 
import time

class Film: 
    def __init__(self, categorie:str,price:float, code: int, passDay: float):
        self.categorie = categorie
        self.price = price
        self.code = code
        self.passDay = passDay

def filmList():
    list_films = []
    film = Film("FAVORITOS",2.50,1,0.50)
    film2 = Film("NUEVOS",3.00,2,0.75)
    film3 = Film("ESTRENOS",3.50,3,1.00)
    film4 = Film("SUPERESTRENOS",4.00,4,1.50)
    list_films.append(film)
    list_films.append(film2)
    list_films.append(film3)
    list_films.append(film4)
    return list_films


def showFilmList():
    nameFilms = ["FAVORTIOS", "NUEVOS", "ESTRENOS", "SUPERESTRENOS"]
    codeFilms = [1,2,3,4]
    print(nameFilms)
    print(codeFilms)
    code = int(input('INTRODUZCA EL CODIGO: '))
    return code

def shearchFilms():
    film_list = filmList()
    code = showFilmList()
    for f in film_list:
        if code == f.code:
            return f
        
def calculatePassDayFilm():
    film = shearchFilms()
    print('La pelicula con el código ' + str(film.code)+ 'es un ' + film.categorie + 'que su coste es'+str(film.price)+ ' su coste de atraso es ' + str(film.passDay))
    numPassDays = int(input('Cuantos de atraso de la devolución has tenido: '))
    filmPriceWithRetard = (film.passDay*numPassDays)+film.price
    return filmPriceWithRetard

def mainFilmFunction():
    calculate = calculatePassDayFilm()
    total_price = 0
    
    total_price = total_price + calculate
    print('El precio total de los atrasos es ' + str(total_price))

    num = int(input('Si desea continuar pulse 1 si no pulse otro numero: '))
    
    while num != 0:
        if num == 1:
            calculate = calculatePassDayFilm()
            total_price = total_price + calculate
            print('El precio total de los atrasos es ' + str(total_price))
        else:
            print('El programa finalizara...')
            time.sleep(3)
            exit()
        num = int(input('Si desea continuar pulse 1 si no pulse otro numero: '))


def main(): 
   mainFilmFunction()

# Execute main() function
if __name__ == '__main__':
    main()

