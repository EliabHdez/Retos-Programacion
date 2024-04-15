""" 
    Implementa los mecanismos de introducción y recuperación de elementos propios de las pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array o lista (dependiendo de las posibilidades de tu lenguaje).
    
    DIFICULTAD EXTRA (opcional):
    - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
      de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
      que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
      Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
      el nombre de una nueva web.
"""

# https://ttmotosrefaccionaria.com.mx
# https://ttmotosrefaccionaria.com.mx/inicio
# https://ttmotosrefaccionaria.com.mx/catalogo

# SIMULACION NAVEGACION SIN UTILIZAR PILAS O COLAS

def simulacion_navExplorador():
    seleccion = input('1.- Ir a la página principal\n2.- Salir\nSelecciona la opción deseada: ')
    
    if seleccion == '2' or seleccion.lower() == 'salir':
        print('Saliendo\nGracias por visitar nuestro sitio web.\nQue tenga buen día\nSaludos')
        
    elif seleccion == '1':
        
        main_page = '--- https://ttmotosrefaccionaria.com.mx ---\n"Bienvenido a TT Motos Refaccionaria"'
        print(main_page)

        if main_page:
            adelante = input('Para ir a la siguiente pestaña escribe "adelante": ')
            adelante.lower()
            
            while adelante != 'adelante':
                print('Error de navegación')
                adelante = input('Para ir a la siguiente pestaña escribe "adelante"')
                adelante.lower()
                
            if adelante == 'adelante':
                start_page = '--- https://ttmotosrefaccionaria.com.mx/inicio ---\n"En TT Motos encontraras todas las refacciones necesarias para tu motocicleta. Cubrimos casi todas las marcas y lo mejor casi todas las cilindradas del mercado"'
                print(start_page)
                
                if adelante:
                    next_decision = input('1.- Regresar a la página principal -> Escribe "atras"\n2.- Ir a la pestaña "Catálogo" -> Escribe "adelante"\nEscribe tu respuesta: ')
                    next_decision = next_decision.lower()
                    
                    if next_decision == 'atras':
                        main_page = '--- https://ttmotosrefaccionaria.com.mx ---\n"Bienvenido a TT Motos Refaccionaria"'
                        print(main_page)
                        simulacion_navExplorador()
                        
                    elif next_decision == 'adelante':
                        catalogo_page = '--- https://ttmotosrefaccionaria.com.mx/catalogo ---\n"En TT Motos Refaccionaria tenemos un amplio catalogo y extenso surtido de refacciones para todas las motocicletas tanto nacionales como importadas"'
                        print(catalogo_page)
                        
                        if adelante:
                            next_decision = input('1.- Regresar a la pestaña inicio -> Escribe "atras"\n2.- Salir" -> Escribe "salir"\nEscribe tu respuesta: ')
                            
                            if next_decision == 'atras':
                                start_page = '--- https://ttmotosrefaccionaria.com.mx/inicio ---\n"En TT Motos encontraras todas las refacciones necesarias para tu motocicleta. Cubrimos casi todas las marcas y lo mejor casi todas las cilindradas del mercado"'
                                print(start_page)
                                
                            elif next_decision == '2'or next_decision.lower() == 'salir':
                                print('Saliendo\nGracias por visitar nuestro sitio web.\nQue tenga buen día\nSaludos')
                                
                            else:
                                print('Opción no válida. Saliendo de la pagina web y cerrando el programa')
                                
                    else:
                        print('Opción no válida. Solo se admite "adelante o atras" para las opciones de respuesta')
                        
    else:
        print('Opción no válida')
        
    
# simulacion_navExplorador()

# SIMULACION NAVEGACION WEB CON EL PRINICIPIO DE PILAS 1

""" Estaba haciendo mal el ejercicio. No lo estaba haciendo con el principio de pilas """

def atras_adelante():
    web_pages = ['https://ttmotosrefaccionaria.com.mx']
    print(f'--- {web_pages[0]} ---')
    print("Bienvenido a TT Motos Refaccionaria")
    
    next_page = input('Para navegar a la pestaña de inicio escribe "adelante": ')
    next_page = next_page.lower()
    
    while next_page != 'adelante':
        print('La única opción disponible a escribir es "adelante"')
        next_page = input('Para navegar a la pestaña de inicio escribe "adelante": ')
        next_page = next_page.lower()
    
    if next_page == 'adelante':
        web_pages.append('https://ttmotosrefaccionaria.com.mx/inicio')
        print(web_pages[-1])
        print("Inicio")
        print('1.- Regresar a la página principal -> Escribe "atras"\n2.- Ir a la pestaña "Catálogo" -> Escribe "adelante"')
        next_page = input()
        next_page = next_page.lower()
        
        if next_page == 'atras':
            web_pages.pop()
            print(web_pages[-1])
            
        elif next_page == 'adelante':
            web_pages.append('https://ttmotosrefaccionaria.com.mx/catalogo')
            print(web_pages[-1])
            print("Catálogo")
            print('1.- Regresar a la pestaña "Inicio" -> Escribe "atras"\n2.- Salir -> Escribe "salir"')
            next_page = input()
            next_page = next_page.lower()
            
            if next_page == 'atras':
                web_pages.pop()
                print(web_pages[-1])
                
            elif next_page == 'salir':
                print('Saliendo...\nGracias por visitar nuestros sitio web.')
                
            else:
                print('Opción no válida. Cerrando el programa')

# atras_adelante()

# https://ttmotosrefaccionaria.com.mx
# https://ttmotosrefaccionaria.com.mx/inicio
# https://ttmotosrefaccionaria.com.mx/catalogo

# web_pages = ['https://ttmotosrefaccionaria.com.mx/']

# SIMULACION NAVEGACION WEB CON EL PRINICIPIO DE PILAS 2

web_pages = []

def pages_aleatorias():
    count = 0
    pages_count = 580
    while count < 5:
        pages_count += 693
        count += 4
        page_aleatoria = f'https://ttmotosrefaccionaria.com.mx/{pages_count}'
        web_pages.append(page_aleatoria)
    
# pages_aleatorias()
# pages_aleatorias('https://ttmotosrefaccionaria.com.mx/')
        
""" print('\nEscribe "pp" para ir a la Página Principal, seguido escribe "adelante" o "atras" para navegar entre las diferentes páginas de la página web')

answer = input().lower()

while answer != 'pp':
    print('Es necesario primero ir a la Página Principal')
    answer = input().lower()

if answer == 'pp':
    web_pages.append('https://ttmotosrefaccionaria.com.mx')
    print(web_pages[0])
    print('Bienvenido a TT Motos Refaccionaria')
    print('Para navegar entre la diferentes pagina de nuestra web solo necesitas escribir "adelante" o "atras". Para salir escriba "exit')
    answer = input().lower()
    
    if answer == 'exit':
        print('Saliendo...')
        print('Gracias por visitar nuestra pagina web')
        
    while answer == 'atras':
        print('No se puede ir mas atras')
        answer = input().lower()
        
    count = 1
    
    while answer == 'adelante':
        # pages_aleatorias()
        print(web_pages[count])
        print(len(web_pages))
        answer = input().lower()
        count += 1
        
        while answer == 'atras':
            print(web_pages.pop())
            print(len(web_pages))
            answer = input().lower()
            
        if answer == 'exit':
            print('Saliendo...')
            print('Gracias por visitar nuestra pagina web') """
            
# SIMULACION DE NAVEGACION WEB (SOLUCION BRAIS)

# def web_navigation():

#     stack = []

#     while True:

#         action = input(
#             "Añade una url o interactúa con palabras adelante/atrás/salir: "
#         )

#         if action == "salir":
#             print("Saliendo del navegador web.")
#             break
#         elif action == "adelante":
#             pass
#         elif action == "atrás":
#             if len(stack) > 0:
#                 stack.pop()
#         else:
#             stack.append(action)

#         if len(stack) > 0:
#             print(f"Has navegado a la web: {stack[len(stack) - 1]}.")
#         else:
#             print("Estás en la página de inicio.")

""" 
    - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una impresora compartida que recibe documentos y los imprime cuando así se le indica. La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se interpretan como nombres de documentos.
"""

# web_navigation()

# SIMULACION IMPRESORA EN LINEA

queue_impressions = []

def print_docs():
    
    while True:
        
        print('¿Que desea hacer?\n1.- Añadir archivo a la cola de impresión\n2.- Imprimir archivo\nPara salir teclea "exit"\n\nDigite el número de la opcion deseada:')
        selection = input()
        
        if selection == 'exit':
            break
        
        if selection == '1': 
            while True:
                doc = input('\nIngrese el nombre del archivo a agregar a la cola de impresión: ').lower()
                if doc == 'exit':
                    print('')
                    break
                for element in queue_impressions:
                    if doc == element:
                        print('"Aviso: Ya existe un archivo con ese nombre en la cola de impresión."')
                        break
                else:
                    queue_impressions.insert(0, doc)
                    print(f'"Archivos en la cola de impresion:"')
                    for element in queue_impressions:
                        print(f'- {element.capitalize()}')
                        
        if selection == '2':
            print('\n- Para imprimir el primer documento de la cola de impresión -> Teclee "imprimir"\n- Si desea imprimir un documento en concreto -> Escriba el "nombre" del archivo a imprimir')
            while True:
                print('\n"Documentos en la cola de impresión"')
                for element in queue_impressions:
                    print(f' - {element.capitalize()}')
                opc_sel = input('Escriba la opción de su elección: ').lower()
                if opc_sel != 'exit' and opc_sel != 'imprimir':
                    if queue_impressions.count(opc_sel) >= 1:
                        index_doc = queue_impressions.index(opc_sel)
                        doc_impreso = queue_impressions.pop(index_doc)
                        print(f'\nDocumento impreso con exito: "{doc_impreso.capitalize()}"')
                    else:
                        print(f'\nEl documento "{opc_sel}" no se encuentra en la cola de impresión\n')
                        break
                if opc_sel == 'exit':
                    print('')
                    break
                if opc_sel == 'imprimir':
                    if len(queue_impressions) == 0:
                        print('\n"No hay documentos en la cola de impresión"')
                    else:
                        doc_impreso = queue_impressions.pop()
                        print(f'\nDocumento impreso con exito: "{doc_impreso.capitalize()}"')
                        
        if selection == 'exit':
            break
                    

print_docs()