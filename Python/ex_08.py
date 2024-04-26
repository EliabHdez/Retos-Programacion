# PILAS Y COLAS

# PILAS/STACK (LIFO - LAST IN, FIRST OUT)

names = []
names.append('Moisés')
names.append('Efrain')
names.append('Nahun')
names.append('Karla')

print(names)

recovery_name = names.pop()
recovery_name = names.pop()
recovery_name = names.pop()
recovery_name = names.pop()

print(names)
print(recovery_name)

# COLAS/QUEUE (FIFO - FIRST IN, FIRST OUT)

names.append('Cortana')
names.append('Nahun')
print(names)
names.insert(1, 'Moises')
print(names)
names.append('Karla')
print(names)
names.insert(3, 'Efrain')
print(names)

names.pop(0)
print(names)
names.remove('Moises')
print(names)
names.pop(2)
print(names)
names.pop(0)
print(names)

# Con pop o remove podemos hacer el efecto de fifo (el primero en entrar es el primero en salir) ya sea pasando el numero de index o el valor tal cual que queremos sacar o eliminar, sin embargo con ambos metodos podemos sacar el elemento que nosotros queramos este en la posicion que este, de igual manera pasando el numero de indice o bien el valor del elemento como tal