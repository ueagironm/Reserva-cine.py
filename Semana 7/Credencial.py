def main():
    usuario = "Richard Giron"
    # Variables booleanas
    sistema_activo = True
    tiene_permiso = True
    print(f"Bienvenido, {usuario}.")
# Evaluación del sistema y del permiso
    if sistema_activo:
        if tiene_permiso:
            print("Acción ejecutada.")
            print(f"Acceso autorizado para {usuario}.")
        else:
            print("Permiso denegado.")
            print("El usuario no tiene permiso para ejecutar la acción.")
    else:
            print("Sistema inactivo.")
            print("No es posible ejecutar la acción.")
    main()
  