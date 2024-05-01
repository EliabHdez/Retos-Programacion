""" 
    EJERCICIO: 
    - Desarrolla un programa de gestión de ventas que almacena sus datos en un archivo .txt.
    - Cada producto se guarda en una línea del archivo de la siguiente manera: [nombre_producto], [cantidad_vendida], [precio].
    - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar, actualizar, eliminar productos y salir.
    - También debe poseer opciones para calcular la venta total y por producto.
    - La opción salir borra el .txt.
"""

fileee=open("C:/Python/Files/Sales/current_sale.txt", "w+")

class Product:
    def __init__ (self,name,quantity,price):
        self.name=name
        self.quantity=quantity
        self.price=price


class Sales_manage:
    def __init__(self):
        self.current_process=None

    def print_in_box(self,message, min_length=50):
        length = max(len(message), min_length)
        print("-" * (length + 4))
        print("|", message.center(length), "|")
        print("-" * (length + 4))



    def create_product(self):
        self.print_in_box("You´re in SALES management, let´s begin adding products...")

        while True:
            try:
                name=input("Product name: ").capitalize()
                quantity=int(input("Quantity sold: "))
                price=int(input("Price: "))
            except:
                    print("")
                    print("------------------------------------>Only numbers must be typped for quantity and price<------------------------------------\n")
            else:
                New_product=Product(name,quantity,price)
                answer=input("Would you like adding another product? (Press enter to continue, type: -no- to finish):  ")
                print("--------------------------------------------------------------------------------------------")
                if answer=="no" or answer=="No":
                    with open("C:/Python/Files/Sales/current_sale.txt", "a") as fileee:
                        total_length =(96)
                        fileee.write("-" * total_length + "\n")
                        fileee.write(f"|    Product: {name.center(30)}|    Quantity: {str(quantity).center(10)}|    Price: ${str(price).center(10)}  |\n")      
                        fileee.write("-" * total_length + "\n")
                    break
                else:
                    with open("C:/Python/Files/Sales/current_sale.txt", "a") as fileee:
                        total_length =(96)
                        fileee.write("-" * total_length +  "\n")
                        fileee.write(f"|    Product: {name.center(30)} |    Quantity: {str(quantity).center(10)}|    Price: ${str(price).center(10)}  |\n")   
                        fileee.write("-" * total_length + "\n")
        print("Printing to verify that everything is as expected:")
        fileee = open("C:/Python/Files/Sales/current_sale.txt", "r+")
        for line in fileee:
            print(line.strip())



sales=Sales_manage()
sales.create_product()















