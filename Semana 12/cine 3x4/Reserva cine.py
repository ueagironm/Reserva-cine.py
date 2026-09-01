"""
Iteración sobre arreglos
multidimensionales utilizando bucles
anidados.
Arreglos N-Dimensionales
Reserva de asiento para
servidor policial Richard Giron en una sala de cine
de 3 filas por 4 columnas (12 asientos en
total).
Estado de cada asiento:
0 = asiento libre
1 = asiento reservado
"""

# Dimensiones de la sala
NUM_FILAS = 3
NUM_COLUMNAS = 4

# 1. Crear la matriz "asientos" como lista de listas,
# inicializada en 0 (libre)
asientos = []
for i in range(NUM_FILAS):
    fila_vacia = [0] * NUM_COLUMNAS
    asientos.append(fila_vacia)

print("=== Sistema de reserva de asientos - Sala de personal policial ===")
print(f"La sala tiene {NUM_FILAS} filas (0 a {NUM_FILAS - 1}) "
      f"y {NUM_COLUMNAS} columnas (0 a {NUM_COLUMNAS - 1}).\n")

# 2. Pedir al usuario la fila y columna del asiento que desea reservar
fila = int(input(f"Ingrese fila del oficial (0 a {NUM_FILAS - 1}): "))
columna = int(input(f"Ingrese columna del oficial (0 a {NUM_COLUMNAS - 1}): "))

# Validación de rango (mejora opcional sugerida en la guía de la tarea)
if 0 <= fila < NUM_FILAS and 0 <= columna < NUM_COLUMNAS:
    # 3. Marcar el asiento como reservado
    if asientos[fila][columna] == 1:
        print("\nAviso: ese asiento ya estaba reservado por otro oficial.")
    else:
        asientos[fila][columna] = 1
        print(f"\nAsiento reservado correctamente para el oficial en fila {fila}, columna {columna}.")
else:
    print("\nError: la fila o columna ingresada está fuera de rango. No se realizó ninguna reserva.")

# 4. Mostrar la matriz completa en formato de tabla usando bucles anidados
print("\nEstado actual de la sala (0 = libre, 1 = reservado):")
for i in range(NUM_FILAS):
    for j in range(NUM_COLUMNAS):
        print(asientos[i][j], end=" ")
    print()  # salto de línea al terminar cada fila