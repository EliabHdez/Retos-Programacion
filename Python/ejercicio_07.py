# RECURSIVIDAD

def recursiva_aLaBaja(num):
    num -= 1
    if num >= 0:
        print(num)
        recursiva_aLaBaja(num)
    else:
        print('Fin de la cuenta regresiva')
    
# recursiva_aLaBaja(101)
        
def factorial_bucle(fact):
    num = 1
    res_num = 2
    while res_num <= fact:
        num *= res_num
        res_num += 1
    return num
    
# print(factorial_bucle(5))

def factorial_recursivo(num):
    if num > 1:
        num = num * factorial_recursivo(num - 1)
    return num
    
# print(factorial_recursivo(5))

def fibonacci(num):
    one_num = 0
    sec_num = 1
    while one_num < num:
        print(one_num)
        next_num = one_num + sec_num
        one_num = sec_num
        sec_num = next_num
        
# fibonacci(100)

def fibonacci():
    prev = 0
    actual = 1
    count = 0
    fib = prev + actual
    prev = actual
    actual = fib
    
    if count <= 50:
        count += 1
        print(prev)
        fibonacci()
    
    
    # while one_num < num:
    #     print(one_num)
    #     next_num = one_num + sec_num
    #     one_num = sec_num
    #     sec_num = next_num
        
# fibonacci()

def fibonacci(number):
    if number <= 0:
        print("La posición tiene que ser mayor que cero")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(8))