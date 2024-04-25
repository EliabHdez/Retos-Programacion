cars = []

print('Pila')

class Pila:
    def __init__(self, car) -> None:
        self.car = car
        cars.append(car)
    
    def imp_list():
        print(cars)
    
    def append_car(self):
        cars.append(self)
        
    def remove_car():
        cars.pop()
        
    def available_cars():
        print(len(cars))
        
    def imp_cars():
        for element in cars:
            print('-',element)
        
dodge = Pila('Stratus')
Mitsubishi = Pila('Lancer Evo')
Volkswagen = Pila('Bora')
Pila.append_car('NSX')
Pila.imp_list()
Pila.append_car('Camaro')
Pila.imp_list()
Pila.remove_car()
Pila.imp_list()
Pila.append_car('Grand Cheroke')
Pila.imp_list()
Pila.available_cars()
Pila.imp_cars()

print('')
print('Cola')

cars_1 = []

class Cola:
    def __init__(self, car) -> None:
        self.car = car
        cars_1.insert(0, car)
    
    def imp_cars():
        print(cars_1)
    
    def append_car(self):
        cars_1.insert(0, self)
        
    def remove_car():
        cars_1.pop()
        
    def available_cars():
        print(len(cars_1))
        
Chevrolet = Cola('Corsa')
Subaru = Cola('Impresa')
Seat = Cola('Leon Cupra')
Cola.append_car('Focus ZX3')
Cola.imp_cars()
Cola.append_car('Cirrus')
Cola.imp_cars()
Cola.remove_car()
Cola.imp_cars()
Cola.append_car('Ram 2500')
Cola.imp_cars()
Cola.remove_car()
Cola.imp_cars()
Cola.available_cars()