##############################################################################################################################################################################################################################
class FILE_Manager:
    def __init__(self):
        self.path = "C:/Python/Files/Sales/current_sale.txt"
##############################################################################################################################################################################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def write_in_txt(self, products_list):    #* Función para actualizar datos despues de realizar una modificacion, tanto del dict como del txt
        from product_manager import Product_NUMBER
        self.class_number = Product_NUMBER()
        with open(self.path, "w") as fileee: #se abre el archivo en modo de escritura "w" para sobreescribir y actulizar la informacion anterior en caso que exista               
            for index, product in enumerate(products_list, start =1): #se utuliza enumerate(comenzando en 1) para utlizar el indice como string en el campo de numero de producto (#)
                #Loop-for para acceder a las propiedades de cada producto, y a su vez ir escribiendo sus datos en el .txt en cada iteracion
                Number_symbol = "#: "         #Variable para dar formato al texto 
                str_product = "Description: " #*utilice este metodo para darle formato de tabla a la info que se escribe en el txt
                str_qty = "Qty: "             #*porque no llegue encotre la manera de darle este mismo formato a la info directamente en consola
                str_price = "Price: "         #*con este metodo, se escriben todos los datos como string en el txt y con la funcion consult()  
                dollar_sign = str("$ ")       #*se leen ya formateados en consola ya que tienen este formato de tabla desde el txt
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
        self.class_sale = SALE_Manager()   #*Instancia para llamar a las funciones de la clase SALE_Manager() (print_in_box())
        #with cierra el archivo automaticamente desde de que se ejecute el bloque
        with open("C:/Python/Files/Sales/current_sale.txt", "r") as fileee:
            #se abre en el archivo en modo lectura
            for line in fileee:
                print(line.strip())  #con .strip() sr eliminan los espacios en blanco al principio y al final de la línea
        print("")
        total_sum=0 #aqui solo se itera sobre la propiedad importt de cada producto para calcularlo
        for product in self.class_number.products_list :
            total_sum+=(product.importt) # y posteriormente mostrarlo mediante un print_in_box
        self.class_sale.print_in_box(f"Total import: ${total_sum}")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
