nombre = input("Introduce tu nombre: ")

print("Buenas" ,nombre,"!")
print("Buenas " + nombre + "!")

print("Buenas " + nombre.upper())
print(f"Buenas  nombre.upper()")
print(f"Buenas  {nombre.upper()}")

print ('Buenas {}'.format(nombre))

def saludar():
   nombre = input('Introduce tu nombre:')
   procedencia = input('Introduce de donde eres:')
   print('Buenas {}!'.format(nombre), f'de {procedencia}!')
 
saludar()