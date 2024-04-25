""" 
    Implementa la jerarquía de una empresa de desarrollo formada por Empleados que pueden ser Gerentes, Gerentes de Proyectos o Programadores.
    
    Cada empleado tiene un identificador y un nombre.
    
    Dependiendo de su labor, tienen propiedades y funciones exclusivas de su actividad, y almacenan los empleados a su cargo.
"""

gerentes_proyectos = []
programadores_karla = []
programadores_janeth = []
programadores_eliab = []

# Superclase Empleados

class Empleados:
    def __init__(self, puesto, nombre, id_empleado):
        self.puesto = puesto
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.empleado = f'{self.nombre} - {self.puesto} - {self.id_empleado}'
        
    def puesto_nombre(self):
        print(f'{self.puesto}:')
        print(f'- {self.nombre}')
        
    def id_empleado(self):
        print(self.id_empleado)
        
    def nombre(self):
        print(self.nombre)
        
    def puesto(self):
        print(self.puesto)
        
    def gerentes_programadores_empresa(self):
        for element in gerentes_proyectos + programadores_karla + programadores_janeth + programadores_eliab:
            print(f'- {element}')
        
    def programadores_empresa_karla(self):
        for element in programadores_karla:
            print(f'- {element}')
            
    def programadores_empresa_janeth(self):
        for element in programadores_janeth:
            print(f'- {element}')
            
    def programadores_empresa_eliab(self):
        for element in programadores_eliab:
            print(f'- {element}')
            
    def personas_cargo(self):
        print(f'El {self.puesto} tiene personal a su cargo.')
            
# Subclase Gerente
            
class Gerente(Empleados):
    def activities(self):
        # print('GERENTE')
        propiedades = 'Propiedad: Persona con mayor poder y responsabilidad en la empresa'
        funciones = 'Funciones:\n - Hacer que toda la empresa funcione al 100%\n - Supervisar tanto los proyectos como a todo el personal\n - Manejar a todo el personal de la empresa'
        print(propiedades)
        print(funciones)
        print('Empleados a su cargo:')
        
# Subclase Gerente de Proyectos
        
class GerentesProyectos(Empleados):
    def activities(self):
        # print('GERENTES DE PROYECTOS')
        propiedades = 'Propiedad: Persona encargada de los proyectos de la empresa'
        funciones = 'Funciones:\n - Supervisar los proyectos asignados\n - Manejar al personal de programación a su cargo'
        print(propiedades)
        print(funciones)
        print('Empleados a su cargo:')
        
    # def personas_cargo(self):
    #     print(f'El {self.puesto} tiene personal a su cargo, dentro de este personal no entra el Gerente')
        
# Subclase Programadores
        
class Programadores(Empleados):
    def activities(self):
        # print('PROGRAMADOR')
        propiedades = 'Propiedad: Son las personas encargadas directamente de desarrollar los proyectos de la empresa'
        funciones = 'Funciones:\n - Desarrollar los proyectos a cargo de la empresa'
        print(propiedades)
        print(funciones)
    
# Creacion de los empleados mediante las clases correspondientes
        
gerente = Gerente('Gerente', 'Efrain Hernández', 'ID 1905')

gerente_proyecto_1 = GerentesProyectos('Gerente de Proyectos de Apps Moviles', 'Karla Cabello', 'ID 2210')
gerente_proyecto = gerente_proyecto_1
gerentes_proyectos.append(gerente_proyecto.empleado)
gerente_proyecto_2 = GerentesProyectos('Gerente de Proyectos de Programas PC', 'Janeth Torres', 'ID 2412')
gerente_proyecto = gerente_proyecto_2
gerentes_proyectos.append(gerente_proyecto.empleado)
gerente_proyecto_3 = GerentesProyectos('Gerente de Proyectos de Videojuegos', 'Eliab López', 'ID 2509')
gerente_proyecto = gerente_proyecto_3
gerentes_proyectos.append(gerente_proyecto.empleado)
# print(gerentes_proyectos)

programador = Programadores('Programador Senior de IA en Python', 'Moisés Hernández', 'ID 2509')
programadores_karla.append(programador.empleado)
programador = Programadores('Programador Junior de Videojuegos en C++', 'Nahun Fernández', 'ID 2910')
programadores_karla.append(programador.empleado)
programador = Programadores('Programador de Apps Moviles IOS', 'Arnulfo Hernández', 'ID 0108')
programadores_janeth.append(programador.empleado)
programador = Programadores('Programador de Apps Moviles Android', 'Lilia López', 'ID 0602')
programadores_janeth.append(programador.empleado)
programador = Programadores('Programador de Maching Learning', 'Isaac López', 'ID 1905')
programadores_eliab.append(programador.empleado)

# Llamando a las clases y las funciones correspondientes para cada uno de los empleados

gerente.puesto_nombre()
gerente.activities()
gerente.gerentes_programadores_empresa()
gerente.personas_cargo()

print('')

gerente_proyecto_1.puesto_nombre()
gerente_proyecto_1.activities()
gerente_proyecto_1.programadores_empresa_karla()
gerente_proyecto_1.personas_cargo()

print('')

gerente_proyecto_2.puesto_nombre()
gerente_proyecto_2.activities()
gerente_proyecto_2.programadores_empresa_janeth()

print('')

gerente_proyecto_3.puesto_nombre()
gerente_proyecto_3.activities()
gerente_proyecto_3.programadores_empresa_eliab()

print('')

programador.activities()

print('')
print('* Desempaquetando los programadores para tenerlos por separado *')
print('')

# Asignando a cada uno de los programadores que conforman el equipo de desarrollo de la empresa a una variable por separado

# Esto lo podriamos hacer la misma manera que hicimos con los gerentes de proyectos, asignarlos a una variable por separado y reasignar esa variable a una variable igual despues de cada uno para que esta nos sirva para la asignacion a la lista, sin embargo lo hice y dejo de esta manera para tener ambas formas. Hay que aclarar que de esta manera, no conservamos el tipo de dato, es decir, que ahora las variables de programadores ya no son una subclase, ahora ya solo son strings y esto es porque al desempaquetarlos de la lista, solo se desempaqueta el contenido en forma de string y no como tal el tipo que contiene los datos, caso contrario de lo que se hizo con los gerentes de proyecto. Esto repercute en que con las variables de los programadores ya no podemos seguir trabajando con los atributos y metodos de la superclase en ellos, caso contrario de los gerentes de proyecto donde si lo podemos hacer

programador_1, programador_2, programador_3, programador_4, programador_5 = programadores_karla + programadores_janeth + programadores_eliab

print(programador_1)
print(programador_2)
print(programador_3)
print(programador_4)
print(programador_5)

print(type(gerente_proyecto_1))
print(type(gerente_proyecto))
print(type(programador))
print(type(programador_1))

print(gerente_proyecto.nombre) # Esta es la variable general que utilizamos para asignar a la lista a los gerentes de proyecto y que fue cambiando cada vez que creabamos uno, es por eso que como resultado nos arroja el ultimo gerente de proyecto creado
gerente_proyecto_1.puesto_nombre() # Esta es la variable que fue asignada de forma individual

# Pero en ambos casos podemos seguir trabajando con los atributos y los metodos de la superclase, ya que siguen siendo de tipo subclase, caso contrario de las variables de programadores donde podemos ver que su tipo es str