#practica_no1.py
# autor: Cristian Echevarria
# fecha: 2026-03-01
# descripcion: Ejercicios de programacion logica

from functools import reduce 

# Ejercicio 1
def suma(a,b):
    """
    Calcula la suma de dos números
    """
    return f'resultado de suma {a} + {b} = {a + b}'
print("....::::: Ejercicio 1 :::::....")
print(suma(1,2))
print('\n')

# Ejercicio 2
def factorial(n):
    """
    Calcula el factorial de un número n ,Se calcula mediante la fórmula n! = n * (n-1)!, con el caso especial de 0! = 1
    """
    # caso base
    if n == 0:
        return 1
    else:
        # caso recursivo
        return n * factorial(n-1)

print("....::::: Ejercicio 2 :::::....")
print(f'factorial de 5: {factorial(5)}') # 5! = 5 * 4 * 3 * 2 * 1 = 120
print('\n')

#Ejercicio 3 # esta funcion me costo un poco entenderla
def fibonacci(n):
    """
    Calcula el número n de la secuencia de Fibonacci
    F(n) = F(n-1) + F(n-2)
    """
    # caso base 1 
    if n == 0:
        return 0
    # caso base 2
    elif n == 1:
        return 1
    else:
        # caso recursivo
        return fibonacci(n-1) + fibonacci(n-2)

print("....::::: Ejercicio 3 :::::....")
print(f'fibonacci de 4: {fibonacci(5)}')
print('\n')

# Ejercicio 4 - espero sea valido lambda :D
print("....::::: Ejercicio 4 :::::....")
lista = [1,2,3,4,5,6,7,8,9,10]
# Generamos una nueva lista con los cuadrados de cada número usando map.
cuadrados = list(map(lambda x: x**2, lista))
print(f'cuadrados: {cuadrados}')

# Filtramos los números pares usando filter
pares = list(filter(lambda x: x % 2 == 0, lista))
print(f'pares: {pares}')

# Usamos reduce para calcular:
# - La suma de [1..10]
suma_lista = reduce(lambda x, y: x + y, lista)
print(f'suma de [1..10]: {suma_lista}')

# - El producto [1..5]
producto_lista = reduce(lambda x, y: x * y, lista[:5])
print(f'producto de [1..5]: {producto_lista}')
print('\n')