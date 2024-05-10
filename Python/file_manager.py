#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class FILE_Manager:
    def __init__(self):
        self.path = "C:/Python/Files/Sales/current_sale.txt"
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def write_in_txt(self, products_list):    #* Función para actualizar datos despues de realizar una modificacion, tanto del dict como del txt
        from product_manager import Product_NUMBER
        self.class_number = Product_NUMBER()
        with open(self.path, "w") as fileee:                
            for index, product in enumerate(products_list, start =1):
                #Loop-for para acceder a las propiedades de cada producto contenido en el dict ya actualizado, y a su vez actualizar los datos en el .txt
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
    def consult(self): #* Funcion simple para consultar todos los productos (planeo agregar la opcion para consultar por numero o nombre de producto)
        from product_manager import Product_NUMBER
        self.class_number = Product_NUMBER()
        from sale_manager import SALE_Manager
        self.class_sale = SALE_Manager()   #*Instancia para llamar a la clase SALE_Manager() y sus funciones dentro de esta funcion
        with open("C:/Python/Files/Sales/current_sale.txt", "r") as fileee:
            for line in fileee:
                print(line.strip())
        print("")
        total_sum=0
        for product in self.class_number.products_list :
            total_sum+=(product.importt)
        self.class_sale.print_in_box(f"Total import: ${total_sum}")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
