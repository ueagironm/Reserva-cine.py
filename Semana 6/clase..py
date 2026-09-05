nombre = "richard giron"
edad = 33
es_policia = False

print("Nombre:", nombre)
print("Edad:", edad)
print("Es policia:", es_policia)

#and 
print("Puede ingresar:", edad >= 18 and es_policia == False)
print("resultado es verdadero")

if edad >= 18 and es_policia == True:
    print("si Puede ingresar a la institución.")
else:
    print("menos de 18 años no puede ingresar a la institución.")