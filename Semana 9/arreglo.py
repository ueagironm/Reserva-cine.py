# Arreglo de cantidades y elementos policiales
cantidades = [10, 20, 30, 40, 50]
elementos = ["Patrulleros", "Radios", "Chalecos", "Motos", "Pistolas"]

# Mostrar el valor en la posición 1 del arreglo (índice 1)
print("Elemento en la posición 1:")
print(cantidades[1], elementos[1])

print("\nRecorrido completo del arreglo:")

# Recorrer todo el arreglo dinámicamente usando el índice i
for i in range(len(cantidades)):
    print(cantidades[i], elementos[i])