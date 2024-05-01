""" 
    EJERCICIO: 
    - Desarrolla un programa de gestión de ventas que almacena sus datos en un archivo .txt.
    - Cada producto se guarda en una línea del archivo de la siguiente manera: [nombre_producto], [cantidad_vendida], [precio].
    - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar, actualizar, eliminar productos y salir.
    - También debe poseer opciones para calcular la venta total y por producto.
    - La opción salir borra el .txt.
"""

file=open("C:/Python/Files/Sales/current_sale.txt", "w+")

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
        while quantity!=int() or price!=int():
            name=input("Product name: ").capitalize()
            quantity=int(input("Quantity sold: "))
            price=int(input("Price: "))
            if quantity!=int() or price!=int():
                print("------------------------------------>Only numbers must be typped for quantity and price<------------------------------------\n")
        else:
            New_product=Product(name,quantity,price)
            file.write(f"[Product: {name}] -> [Quantity: {quantity}] -> [Price: ${price}]")








#        file.write(f"[Product: {name}] -> [Amount: {quantity}] -> [Unit Price: ${price}]")




sales=Sales_manage()
sales.create_product()















