#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#ependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre=input("ingrese su nombre: ")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
numero=input("ingrese el numero 1,2 o 3: ")
numero=int(numero)
if(numero==1):
   print(nombre.upper())
elif(numero==2):
   print(nombre.lower())
elif(numero==3):
   print(nombre.capitalize())
else:
   print("porfavor ingrese 1,2 o 3")

