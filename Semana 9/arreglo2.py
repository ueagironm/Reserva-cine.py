# 1. Crear el arreglo (lista) con las cadenas de texto
equipos = ["10 patrullas", "20 radios", "30 chalecos", "40 motos", "50 pistolas"]

# 2. Mostrar el elemento almacenado en la posición 1 (índice 1)
# Índice 0 -> "10 patrullas"
# Índice 1 -> "20 radios"
print("El elemento en la posición 1 es:", equipos[1])

print("\n--- Recorrido del arreglo ---")

# 3. Recorrer todo el arreglo e imprimir cada elemento
for equipo in equipos:
    print(equipo)