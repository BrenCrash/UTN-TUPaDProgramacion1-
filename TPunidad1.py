# Práctico 1: Estructuras secuenciales
# Alumna: Brenda Florencia Romero

# Ejercicio 1

print ("Hola mundo")


# Ejercicio 2

nombre = input ("(Por favor, ingresa tu nombre:")

print (f"Hola {nombre}!")


# Ejercicio 3

apellido = input("Ingresa tu apellido:")
edad = input ("Ingresa tu edad:") 
residencia = input ("Ingresa tu lugar de residencia:")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# Ejercicio 4

radio = float(input(" Ingresa el radio del circulo: "))

import math
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio


print("El área del círculo es:", round(area, 2))
print("El perímetro del círculo es:", round(perimetro, 2))



# Ejercicio 5 

segundos = float(input("Ingrese la cantidad de segundos: "))

horas = segundos / 3600     # 1 hora = 3600 segundos

print ("Equivale a " , round (horas, 2) , "horas. ")


# Ejercicio 6

número = int(input( "Ingrese un número para ver su tabla de multiplicar: ") )

print(f"\nTabla de multiplicar del {número}:\n")
for i in range(1, 11):
    resultado = número * i
    print(f"{número} x {i} = {resultado}")
    
    
    
    
    # Ejercicio 7
    
   

num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))


if num1 != 0 and num2 != 0:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2  

    
    print(f"\nResultados de las operaciones entre {num1} y {num2}:")
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {round(division, 2)}")
else:
    print("Error: ambos números deben ser distintos de cero.")


# Ejercicio 8


peso = float(input(" Ingresa tu peso en kilogramos: "))
altura= float(input(" Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

print (f" Tu indice de masa corporal es {imc:.2f}")



# Ejercicio 9

Celsius = float(input(" Ingresa  la temperatura en grados Celsius: "))

fahrenheit = (9 / 5) * Celsius + 32

print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}°F")


# Ejercicio 10

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

promedio = (num1 + num2 + num3) / 3


print(f"El promedio de los tres números es: {promedio:.2f}")

