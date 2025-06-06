nombre1 = input("Introduce tu nombre usuario1: ")
nombre2 = input("Introduce tu nombre usuario2: ")
accion1 = input("Usuario1, piedra, papel o tijeras: ")
accion2 = input("Usuario2, piedra, papel o tijeras: ")

accion1 = accion1.lower()
accion2 = accion2.lower()

if accion1 == accion2:
    print("Ambos han seleccionado la misma opción.")
elif accion1 == 'piedra':
    if accion2 == 'papel':
        print("Gana " + nombre2)
    elif accion2 == 'tijeras':
        print("Gana " + nombre1)
elif accion1 == 'papel':
    if accion2 == 'piedra':
        print("Gana " + nombre1)
    elif accion2 == 'tijeras':
        print("Gana " + nombre2)
elif accion1 == 'tijeras':
    if accion2 == 'piedra':
        print("Gana " + nombre2)
    elif accion2 == 'papel':
        print("Gana " + nombre1)