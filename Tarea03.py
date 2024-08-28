#Tarea 03

mi_diccionario = {
    "nombre": "Sebas",
    "edad": 21,
    "ciudad": "Coacalco"
}

# 1. pop()
edad = mi_diccionario.pop("edad")
print(f"pop: {edad}")  # Imprime la edad asignada a edad
print(f"Diccionario después de pop: {mi_diccionario}")

# 2. get()
ciudad = mi_diccionario.get("ciudad")
print(f"get: {ciudad}")

# 3. copy()
copia_diccionario = mi_diccionario.copy()
print(f"copy: {copia_diccionario}")

# 4. keys()
claves = mi_diccionario.keys()
print(f"keys: {claves}")

# 5. items()
items = mi_diccionario.items()
print(f"items: {items}")  #

# 6. clear()
mi_diccionario.clear()
print(f"clear: {mi_diccionario}")

# Reiniciando el diccionario
mi_diccionario = {"nombre": "Juan", "edad": 18, "ciudad": "San Esteban"}

# 7. fromkeys()
nuevas_claves = ["a", "b", "c"]
nuevo_diccionario = dict.fromkeys(nuevas_claves, 0)
print(f"fromkeys: {nuevo_diccionario}")

# 8. popitem()
ultima_clave, ultimo_valor = mi_diccionario.popitem()
print(f"popitem: Clave - {ultima_clave}, Valor - {ultimo_valor}")
print(f"Diccionario después de popitem: {mi_diccionario}")

# 9. setdefault()
pais = mi_diccionario.setdefault("pais", "España")
print(f"setdefault: {pais}")
print(f"Diccionario después de setdefault: {mi_diccionario}")

# 10. update()
mi_diccionario.update({"edad": 26, "ciudad": "Barcelona"})
print(f"update: {mi_diccionario}")

# 11. values()
valores = mi_diccionario.values()
print(f"values: {valores}")
