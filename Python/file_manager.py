fileee=open("C:/Python/Files/Sales/current_sale.txt", "w+")   #* Recien se ejecuta el programa se crea el archivo .txt sobre el cual se trabajará
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class FILE_Manager:
    def __init__(self):
        self.path = "C:/Python/Files/Sales/current_sale.txt"
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def write_products_in_txt(self):
        from product_manager import Product_NUMBER
        self.class_number = Product_NUMBER()
        with open(self.path, "w") as fileee:                 
            for index, product in self.class_number.products_dict.items():  #Loop-for para acceder a las propiedades de cada producto contenido en el dict ya actualizado, y a su vez actualizar los datos en el .txt
                Number_symbol = "#: "         #Variable para dar formato al texto 
                str_product = "Description: " #Variable para dar formato al texto 
                str_qty = "Qty: "             #Variable para dar formato al texto 
                str_price = "Price: "         #Variable para dar formato al texto 
                dollar_sign = str("$ ")       #Variable para dar formato al texto
                str_importt = "Import: "      #Variable para dar formato al texto
                product_info = f"|  {(str(Number_symbol)+str(index)).center(4)}  |  {(str(str_product)+(product.name)).center(47)}  |  {(str(str_qty)+str(product.quantity)).center(10)}  |  {((str_price)+str(dollar_sign)+str(product.price)).center(15)}  |  {((str_importt)+str(dollar_sign)+str(product.importt)).center(15)}  |"
                fileee.write("-" * 117 + "\n")                                                   
                fileee.write(f"{product_info}\n")  #Se escribe la info con formato de tabla en el .txt                                
                fileee.write("-" * 117 + "\n")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def print_total_in_txt(self):
        from product_manager import Product_NUMBER
        self.class_number = Product_NUMBER()
        total_sum=0
        for index, product in self.class_number.products_dict.items():
            product=self.class_number.get_product(index)
            total_sum+=(product.importt)
        str_total = "Total: "
        total_info = (f"|{(str(str_total)+str(total_sum)).center(115)}|")
        self.class_number.update_products()   #Con la funcion update_info borramos en el txt la info anterior (lo cual es necesario si es la segunda ves que se escribe despues de salir al menu de navegacion)
        with open(self.path, "a") as fileee: #Ya que la primera vez que se sale, en automatico se escirbe al final el total en el txt y este quearía ahi si no se actualiza
            fileee.write("-" * 117 + "\n")
            fileee.write(f"{total_info}\n")
            fileee.write("-" * 117 + "\n")