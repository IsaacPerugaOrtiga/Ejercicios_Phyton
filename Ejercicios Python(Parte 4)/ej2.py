"""De la galería de productos, el usuario introducirá el código y el número de unidades del producto que desea comprar. 
El programa determinará el total a pagar, como una factura.
Una variante a este ejercicio que lo haría un poco más complejo sería dar 
la posibilidad de seguir ingresando diferentes códigos de productos con sus respectivas cantidades, 
y cuando el usuario desee terminar el cálculo de la factura completa con todas sus compras. Te animas??"""

def showProductList():
    print("ELIJA EL PRODUCTO DESEADO\n")
    print("PRODUCTOS\n")
    products = ["CAMISA", "CINTURON", "ZAPATOS", "PANTALON", "CALCETINES","FALDAS","GORRAS","SUETER","CORBATA","CHAQUETA"]
    productsCode = [1,2,3,4,5,6,7,8,9,10]
    code = int(input("INTRODUZCA CODIGO: "))
    return code

def searchProductPrice():
    product_list = productList()
    # for i in product_list:



def productList():
    product = Product(1,"CAMISA",15.00)
    product2 = Product(2,"CINTURON",5.00)
    product3 = Product(3,"ZAPATOS",12.00)
    product4 = Product(4,"PANTALON",15.50)
    product5 = Product(5,"CALCETINES",4.25)
    product6 = Product(6,"FALDAS",7.00)
    product7 = Product(7,"GORRAS",6.00)
    product8 = Product(8,"SUETER",23.00)
    product9 = Product(9,"CORBATA",8.00)
    product10 = Product(10,"CHAQUETA",30.00)
    product_list = []
    product_list.append(product)
    product_list.append(product2)
    product_list.append(product3)
    product_list.append(product4)
    product_list.append(product5)
    product_list.append(product6)
    product_list.append(product7)
    product_list.append(product8)
    product_list.append(product9)
    product_list.append(product10)
    return product_list


class Product:
    def __init__(self,codeProduct:int,descProduct:str,price:float):
        self.codeProduct = codeProduct
        self.descProduct = descProduct
        self.price = price