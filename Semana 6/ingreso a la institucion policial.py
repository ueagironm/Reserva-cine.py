def main():
    nombre = "richard giron"
    edad = 18
    tiene_documento = True

    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Tiene documento:", tiene_documento)

    if edad >= 18 and tiene_documento == True:
        print("si Puede ingresar a la institución.")
    else:
        print("No puede ingresar.")

# Ejecución obligatoria
if __name__ == "__main__":
    main()