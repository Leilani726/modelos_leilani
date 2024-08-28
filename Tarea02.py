# tarea02.py

# Definimos un rango de ejemplo
r = range(0, 10)

# 1. Mutabilidad: Intentaremos cambiar un elemento del rango
try:
    r[0] = 100
    es_mutable = True
except TypeError:
    es_mutable = False

# 2. Suma: Intentaremos sumar dos rangos
try:
    r_sum = r + range(10, 20)
    se_puede_sumar = True
except TypeError:
    se_puede_sumar = False

# 3. Producto por un entero: Intentaremos multiplicar un rango por un entero
try:
    r_mult = r * 2
    se_puede_multiplicar = True
except TypeError:
    se_puede_multiplicar = False

# 4. Slicing: Intentaremos hacer slicing en el rango
try:
    r_slicing = r[2:5]
    se_puede_slicing = True
except TypeError:
    se_puede_slicing = False

# 5. Convertir a lista o tupla
r_lista = list(r)
r_tupla = tuple(r)

# 6. Función len: Verificaremos la longitud del rango
r_len = len(r)

# Resultados
print(f"Mutabilidad: {es_mutable}")
print(f"Suma: {se_puede_sumar}")
print(f"Producto por un entero: {se_puede_multiplicar}")
print(f"Slicing: {se_puede_slicing}")
print(f"Lista: {r_lista}")
print(f"Tupla: {r_tupla}")
print(f"Longitud: {r_len}")
