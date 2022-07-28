#Realizaré un programa que ayude al usuario a pedir información sobre mí.
print("\t.:Mi historieta:.")
print()
nombre = input("¿Me dices tu nombre? ")
print("Hola " + nombre + ", puedes hacerme una pregunta del siguiente menu de opciones:")
print("1. ¿Cómo te llamas?")
print("2. ¿Dónde vives?")
print("3. ¿Qué estudiaste?")
print("4. ¿Tacos o Pizza?")
print("5. Salir")
print()
opcion = int(input("Elige una pregunta: "))
minombre = str("Sócrates")
vive = str("CDMX")
estudio = str("Sistemas informaticos")
food = str("tacos")
salir = int(5555555555)
bandera = True
while bandera == True:
  if opcion == 1:
    print("Mi nombre es " + minombre)
    opcion = int(input("Elige otra pregunta: "))
  elif opcion == 2:
    print("Vivo en " + vive)
    opcion = int(input("Elige otra pregunta: "))
  elif opcion == 3:
    print("Estoy estudiando " + estudio)
    opcion = int(input("Elige otra pregunta: "))
  elif opcion == 4:
    print("Obviamente " + food)
    opcion = int(input("Elige otra pregunta: "))
  elif opcion == 5:
    print("Adios")
    bandera = False