print("¿Cual es su nombre?")
nombre = input()

print(f"Hola señor/a {nombre}")

print("¿Que tabla de multiplicar quiere?")
z = int(input("Numero de la tabla: "))

print(("¿Hasta que numero quiere la tabla?"))
x = int(input("Ingrese numero final: "))

for i in range(1,x + 1):
    print(f"{i} multiplicado por {z} es igual a {i * z}")

print("Gracias por utilizar nuestro programa 😀")
    