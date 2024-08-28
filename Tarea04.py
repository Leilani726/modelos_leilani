# tarea04.py

# Ejercicio 1: Calcular el promedio ponderado de las calificaciones
calif_1 = 10
calif_2 = 7
calif_3 = 4

# Pesos de las calificaciones
peso_1 = 0.15
peso_2 = 0.35
peso_3 = 0.50

# Cálculo del promedio ponderado
promedio_ponderado = (calif_1 * peso_1) + (calif_2 * peso_2) + (calif_3 * peso_3)

# Imprimir el resultado
print("El promedio es:", promedio_ponderado)

# Ejercicio 2:
matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]

for fila in matriz:
    suma = fila[0] + fila[1] + fila[2]
    fila[3] = suma

print("Matriz corregida:")
for fila in matriz:
    print(fila)
