
# Práctico 4: Estructuras repetitivas
# Alumna: Brenda Florencia Romero


# Ejercicio 1:

for numero in range(101):
    print(numero)
    



# Ejercicio 2:

numero = input(" Ingrese un número entero: ")

# Vamos a eliminar el signo negativos caso haya.
numero_sin_signo = numero.lstrip('-')

if numero_sin_signo.isdigit():
    cantidad_de_digitos = len(numero_sin_signo)
    print(f"El número tiene {cantidad_de_digitos} dígito(s).")
else:
    print("Ingrese un número entero válido.")
    




# Ejercicio 3:

inicio = int(input(" Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

if inicio > fin:
    inicio, fin = fin, inicio
    

suma = 0

for numero in range(inicio + 1, fin) :
    suma += numero
    

print (f"La suma de los números entre {inicio} y {fin}, excluyéndolos, es: {suma}3")




# Ejercicio 4:


total = 0

while True:
    numero = int(input("Ingresa un número entero (0 para terminar): "))
    if numero == 0:
        break
    total += numero

print(f"La suma total de los números ingresados es: {total}")


# Ejercicio 5:

        
             
import random


numero_secreto = random.randint(0, 9)
intentos = 0

print("¡Adiviná el número secreto entre 0 y 9!")

while True:
    intento = int(input("Tu intento: "))
    intentos += 1

    if intento == numero_secreto:
        print(f"¡Correcto! El número era {numero_secreto}. Lo adivinaste en {intentos} intento(s).")
        break
    else:
        print("No es ese... ¡intentá de nuevo!")
        
        
        
# Ejercicio 6:


for numero in range(100, -2, -1):
    print (numero)       
        



# Ejercicio 7:


limite = int(input("Ingresá un número entero positivo: "))


if limite >= 0:
    suma = 0
    for numero in range(limite + 1):
        suma += numero
    print(f"La suma de los números entre 0 y {limite} es: {suma}")
else:
    print("Por favor, ingresá un número entero positivo.")
    


# Ejercicio 8:



cantidad = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingresá {cantidad} números enteros:")

for i in range(cantidad):
    numero = int(input(f"Número {i + 1}: "))

    # Contar pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Contar positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResultados:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")




# Ejercicio 9:

    
cantidad = 100

suma_total = 0

print(f"Ingrsá {cantidad} números enteros:")

for i in range(cantidad):
    numero = int(input(f"Número {i + 1}: "))
    suma_total += numero

media = suma_total / cantidad

print("\nResultado:")
print(f"La media de los {cantidad} números ingresados es: {media}")



# Ejercicio 10:


numero = input("Ingresá un número entero: ")
numero_invertido = numero[::-1]

print("Número invertido:", numero_invertido)

























    