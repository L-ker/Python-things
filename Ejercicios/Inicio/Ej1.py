from datetime import date

nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
ano = date.today().year

anoNacimiento = int(ano) - int(edad)
anoCon100 = str(anoNacimiento + 100)

print("Hola " + nombre + ", tendrás 100 años en " + anoCon100)