# --- Herencia y Polimorfismo ---

# Herencia

# La herencia es un proceso mediante el cual se puede crear una clase hija que hereda de una clase padre, compartiendo sus métodos y atributos. Además de ello, una clase hija puede sobreescribir los métodos o atributos, o incluso definir unos nuevos

# El polimorfismo es la facilidad de ocupar los metodos y datos de una superclase en una subclase adecuandolos o cambiandolos a los requerimientos necesitados. Es decir, una funcion o dato en una superclase lo podemos ocupar en una subclase pero esta funcion o dato lo podemos modificar y ponerle algo completamente diferente, por lo tanto se estara comportando como se haya declarado en la subclase y no como se declaro en la superclase. Este ejemplo lo vamos a ver con la función feeding_type en la subclase Shark

class Animal:
    def __init__(self, species, specimen, gender) -> None:
        self.species = species
        self.specimen = specimen
        self.gender = gender
        print(f'- {species}')
        print(f'- {specimen}')
        print(f'- {gender}')
        
    # Si tenemos funciones o datos en una superclase y estos los reutilizamos en una subclase sin generar una modificacion en esta ultima, estariamos haciendo uso de la herencia, vaya, estariamos heredando la funcion de la superclase en la subclase, pero si modificamos la funcion o el dato estariamos haciendo uso del polimorfismo, es decir estamos cambiando el valor del dato o el comportamiento de la funcion de acuerdo a los necesitado en la subclase
        
    def movement_gral(self):
        print('La forma en la que me desplazo es:')
    
    def sound_gral(self):
        print(f'El sonido emitido por el {self.specimen} es:')
    
    def feeding_type(self):
        print(f'El {self.specimen} es un animal carnivoro')
    
    def description(self):
        if self.gender == 'Hembra':
            print(f'Soy un {self.specimen} y pertenezco a la clase "{self.species}". Y soy una {self.gender}')
        if self.gender == 'macho'.capitalize():
            print(f'Soy un {self.specimen} y pertenezco a la clase "{self.species}". Y soy un {self.gender}')
        
print('--- DOG ---')
    
class Dog(Animal):
    def movement(self):
        print('- Caminando')
    
    def sound(self):
        print('  "Wuuaaf"')

dog = Dog('Mamífero', 'Perro', 'macho'.capitalize())
dog.movement_gral()
dog.movement()
dog.description()

print('')
print('--- CAT ---')

class Cat(Animal):
    def movement(self):
        print('- Caminando')
        
    def sound(self):
        print('  "Miaau"')

cat = Cat('Mamífero', 'Gato', 'Hembra')
cat.movement_gral()
cat.movement()
cat.description()

print('')
print('--- SHARK ---')

class Shark(Animal):
    def movement(self):
        print('- Nadando')
        
    def sound(self):
        print('  El tiburon no emite sonidos. Su comunicación es a través del lenguaje corporal')
        
    def feeding_type(self):
        print('Carnívoro') # Esto es el polimorfismo
        
shark = Shark('Ovíparo', 'Tiburón', 'Macho')
shark.movement_gral()
shark.movement()
shark.description()
shark.feeding_type() # Revisar el resultado y comparar lo imprime la esta funcion tanto en la superclase como en la subclase para entender lo que es y hace el polimorfismo

print('')
print('--- EAGLE ---')

class Eagle(Animal):
    def movement(self):
        print('- Volando')
        
    def sound(self):
        print('  El Águila emite un sonido de tipo chillido. Este es dificil de imitar')
        
eagle = Eagle('Ovíparo', 'Águila', 'Hembra')
eagle.movement_gral()
eagle.movement()
eagle.description()

print('')
print('--- SOUNDS ---')

dog.sound_gral()
dog.sound()
print('')

cat.sound_gral()
cat.sound()
print('')

shark.sound_gral()
shark.sound()
print('')

eagle.sound_gral()
eagle.sound()