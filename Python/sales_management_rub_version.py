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
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class Sale_number:                                                                                      #* Esta clase gestiona un diccionario para manejar los productos por orden numérico
    def __init__(self,new_product=None):
        self.products_dict = {}
        if new_product:
            self.add_product(new_product)

    def add_product(self, new_product):                                                                 #Esta función agrega los productos al dict (comenzando con el indice 1 para que coincida con nuestra forma de contar) 
        self.products_dict[len(self.products_dict) + 1] = new_product                                   #Posteriormente en la clase Sales_manage en la función create_product se asocia el indice con la variable sale_number

    def get_product(self, number_by_user):                                                              #Esta función es para obtener un producto determinado (por numero de producto) y hacer lo necesario con sus propiedades
        return self.products_dict.get(number_by_user)
    
class Sales_manage:
    def __init__(self):
        self.clas_sale_number = Sale_number()

    def print_in_box(self,message, min_length=50):                                                      #Funcion para imprimir en consola (con una cajita que centra el contenido automaticamente)
        length = max(len(message), min_length)
        print("-" * (length + 4))
        print("|", message.center(length), "|")
        print("-" * (length + 4))

    def create_product(self):                                                                           #Función general para crear los productos y para escribirlos en el archivo .txt (estoy pensado en separarlas)
        self.print_in_box("You´re in SALES management, let´s begin adding products...")                 #Pero la neta me costó mucho trabajo y funcionan bien asi que mejor no xd
        with open("C:/Python/Files/Sales/current_sale.txt", "w") as fileee:
            fileee.write("")                                                                            #Limpia el archivo antes de agregar nuevos productos
        sale_number = 0  
        while True:                                                                                     #Este Loop es optener la respuesta deseada (se inicia el programa con la obligacion de agregar al menos un producto  
            try:                                                                                        #Ya que es necesario para tener una base mínima con la cual trabajar)
                name = input("Product name: ").capitalize()                                             #Por lo pronto se permite cualquier tipo de caracter para el nombre (incluso espacio vacío, luego soluciono eso xd)
                quantity = int(input("Quantity sold: "))
                price = int(input("Price: "))
            except:
                print("------------------------------------>Only numbers must be typed for quantity and price<------------------------------------\n") #Reglas para el input (respuesta deseada)
            else:
                Number_symbol="#: "                                         
                str_product="Product: "
                str_qty="Qty: "                                                                         #Strings para imprimir todo el tecto formateado en el .txt
                str_price="Price: "
                dollar_sign = str("$ ")

                new_product = Product(name, quantity, price)
                self.clas_sale_number.add_product(new_product)                                          #Se llama la funcion para agregar los productos
                sale_number += 1
                product_info=(f"|  {(str(Number_symbol)+str(sale_number)).center(4)}  |  {(str(str_product)+(name)).center(30)}  |  {(str(str_qty)+str(quantity)).center(10)}  |  {((str_price)+str(dollar_sign)+str(price)).center(15)}  |")
                with open("C:/Python/Files/Sales/current_sale.txt", "a") as fileee:                     #Se escribe todo ya formateado en el .txt (formato de tabla para una mayor facilidad de lectura de datos) 
                        fileee.write("-" * 80 + "\n")                                                   #para que así se imprima en cosola (ese formato de tabla que viene desde el archivo .txt)
                        fileee.write(f"{product_info}\n")   
                        fileee.write("-" * 80 + "\n")
                while True:                                                                             #Este loop es para continuar agregando productos o detenerse            
                    try:
                        print("-----------------------------------------------------------------------------------------")
                        answer = int(input("| Would you like adding another product? (Type: 1 to continue or  2 to finish) |-->  "))
                        print("-----------------------------------------------------------------------------------------")
                    except:
                        self.print_in_box(f"Please, enter just 1 or 2")
                    else:
                        if answer == 2:                                                                 #Si se selecciona 2 (finish) se detiene el loop interior y posteriormente se ejecuta el ultimo comando del loop exterior 
                            break                                                                       #el cual es finally: y que contiene esta misma condicional 
                        if answer == 1:                                                                 
                            self.print_in_box(f"Alright, let´s continue with product # {(sale_number)+1}")##Si se selecciona 1 (continuar) solo se detiene el loop interior que es el que pregunta si se desea continuar o no
                            break

                        else:
                            print("Invalid choice. Please enter 1 or 2.")
            finally:
                    if answer == 2:                                                                     #Si de desea parar y no agregar mas productos se detiene tambien el loop exterior dando seguimiento al loop interior
                            break


    def consult(self):                                                                                  #Funcion simple para consultar todos los productos (planeo agregar la opcion para consultar por numero o nombre de producto)
        with open("C:/Python/Files/Sales/current_sale.txt", "r") as fileee:
            for line in fileee:
                print(line.strip())


    def update_product(self):                                                                           #Funcion para actulizar los datos del prodcuto seleccionado (ya sea nombre, cantidad o precio)
        while True:                                                                                     #Bucle para verificar que el numero de producto realmente exista
            self.print_in_box("Please enter # of the product to update: ")
            number_by_user = int(input("#: "))
            current_product = self.clas_sale_number.get_product(number_by_user)                         #Se llama a la funcion get_product() que es la que se encarga de buscar un producto por numero y lo retorna quedando disponible para hacer modificaciones 
            if current_product:                                                                         #Si el producto existe se procede con el siguiente paso
                while True:                                                                             #Bucle para verificar que se ingrese una opcion valida
                    change = input("What do you need to change? (1: Product name, 2: Quantity sold, 3: Price) Please, enter number selection: ").capitalize()
                    if change == "1" or change == "Name" or change== "Product" or change== "Product name":
                        new_name = input("Enter new product name: ").capitalize().center(50)
                        current_product.name = new_name 
                        self.consult()
                        break
                    elif change == "2" or change == "Quantity" or change== "Qty" or change== "Sold" or change =="Quantity sold" or change =="Qty sold":
                        new_quantity = input("Enter new quantity sold: ").center(50)
                        current_product.quantity = new_quantity
                        self.consult()
                        break                                                                           #Al finalizar la modificacion termina la funcion, tengo pensado modificar el loop para seguir haciendo modificaciones si se desea 
                    elif change == "3" or change=="Price" :                                             
                        new_price = input("(Just numbers, no dollar sign) Enter new price: ").center(50)
                        current_product.price = new_price
                        self.consult()
                        break
                    else:
                        self.print_in_box("Please, enter a valid selection")
                break
            else:
                self.print_in_box("This # sale doesn´t exist. Please, try again")                       #Si el numero de producto ingresado no existe se notifica al usuario y se repite el bucle

    def remove_product (self):
        while True:                                                                                     #Igual que los anteriores loop de verificacion
            try:
                self.print_in_box("Please enter # of the product to remove: ")
                number_by_user=int(input("#: "))
            except:
                self.print_in_box(f"Please enter just a number")
            else:
                if number_by_user in self.clas_sale_number.products_dict:                               #Si el numero de producto dado por el usuario existe:
                    del self.clas_sale_number.products_dict[number_by_user]                             #Se elimina del diccionario
                    updated_products_dict = {}                                                          #Diccionario (temporal) para almacenar los productos actualizados
                    for i, product in enumerate(self.clas_sale_number.products_dict.values(), start=1): #Loop for para recorrer todos los elementos (por indice y producto) del diccionario ya modificado, comenzando por el indice 1 
                        updated_products_dict[i]=product                                                #Para reasignar el # de producto correctamente 

                    self.clas_sale_number.products_dict = updated_products_dict                         #Se llama al diccionario modificado para actualizarlo con la informacion del diccionario temporal

                    with open("C:/Python/Files/Sales/current_sale.txt", "w") as fileee:                 
                        for i, product in self.clas_sale_number.products_dict.items():                  #Loop para acceder a los elemento del diccionario ya actualizado y reescribir los datos actualizados en el .txt
                            Number_symbol = "#: "
                            str_product = "Product: "
                            str_qty = "Qty: "
                            str_price = "Price: "                                                       #Variables para dar formato al texto 
                            dollar_sign = str("$ ")
                            product_info = f"|  {(str(Number_symbol)+str(i)).center(4)}  |  {(str(str_product)+(product.name)).center(30)}  |  {(str(str_qty)+str(product.quantity)).center(10)}  |  {((str_price)+str(dollar_sign)+str(product.price)).center(15)}  |"

                            fileee.write("-" * 80 + "\n")                                               #Se escribe la info con formato de tabla en el .txt                                                  
                            fileee.write(f"{product_info}\n")                                           
                            fileee.write("-" * 80 + "\n")

                    self.consult()
                    break                                                                               #Se rompe el loop una vez teminada la eliminacion del producto, tambien tengo pensado en hacer modificaciones para continuar si se desea
                else:
                    self.print_in_box(f"That sale # doesn´t exist, please try again")
                
            
                                                                                                        #Aún me falata agregar opciones para calcular la venta total y por producto. pero eso el lo mas facil xd, ya pronto quedará con eso la parte de ventas
                                                                                                        #Una vez finalizado pasaré a la parte de inventario 



sales=Sales_manage()                                                                                    #*Por el momento no he agregado un menú de navegacion, para usar las funciones hay que ejecutarlas manualmente
sales.create_product()                                                                                  #Llamando por sales.(la funcion deseada())
sales.consult()
sales.update_product()                                                                                  #Me falta agregar que despues de realizar un cambio lo muestre pero ya es tarde y no me quiero volver a desvelar, tanto xd
sales.remove_product()

                                                                #* HASTA AQUÍ MI REPORTE, JOAQUIN (DIGO, ELIAB JAJAJA)













