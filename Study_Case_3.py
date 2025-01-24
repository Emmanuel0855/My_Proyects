"""
Case Study 7: Lazy Lambda Transformation

• Task: Generate a lazy sequence of natural numbers and apply different 
lambda functions to transform and filter the sequence (e.g., square only 
the odd numbers).
• Hint: Use yield for lazy generation, map() and filter() with lambda for 
transformations and filtering.
"""

# Lazy sequence para numeros naturales usando yield
def LazySequence():
    num = 1
    while True:
        # devolvemos el numero actual
        yield num 
        num += 1 

# usamos filter para obtener solo los numeros pares de los numeros naturales generados
pares = filter(lambda x: x % 2 == 0, LazySequence())

# usamos map para transformar los numeros filtrados y le sumamos 1 para hacerlos impares
impares = map(lambda x: x + 1, pares)

# inicializamos una lista de rango 10 donde meteremos los numeros transformados (impares)
odds = [next(impares) for i in range(10)]

# imprimimos la lista de los primeros 10
print(odds)