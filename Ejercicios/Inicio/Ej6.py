cadena = input("Introduce una frase o número y te diré si es palíndromo: ")

cadenaReversa = ""

for i in range(len(cadena)-1, -1, -1):
    cadenaReversa += cadena[i]

# slicing
# cadenaReversa = cadena[::-1]

if cadena == cadenaReversa:
    print("Es palíndromo")
else:
    print("No es palíndromo")