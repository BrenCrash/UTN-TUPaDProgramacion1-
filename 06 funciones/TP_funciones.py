# Práctico 2: Funciones en Python
# Alumna: Brenda Florencia Romero


# EJERCICIO 1:

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


# EJERCICIO 2:

def saludar_usuario(nombre):
    return f"Hola {nombre}!"


nombre_ingresado = input("Ingresa tu nombre: ")  
saludo = saludar_usuario(nombre_ingresado)       
print(saludo)                                   


# EJERCICIO 3: 


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")


informacion_personal(nombre, apellido, edad, residencia)



# EJERCICIO 4: 


import math

def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro


radio = float(input("Ingresa el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")



# EJERCICIO 5:


def segundos_a_horas(segundos):
    horas = segundos / 3600 
    return horas


segundos = float(input("Ingresa la cantidad de segundos: "))
resultado = segundos_a_horas(segundos)

print(f"{segundos} segundos equivalen a {resultado:.2f} horas.")


# EJERCICIO 6: 



def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):  
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

tabla_multiplicar(numero)



#EJERCICIO 7:


def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)


a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

resultados = operaciones_basicas(a, b)

print("\nResultados de las operaciones:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]:.2f}")




# EJERCICIO 8: 



def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))
resultado = calcular_imc(peso, altura)

print(f"Tu índice de masa corporal (IMC) es: {resultado:.2f}")

#Recordatorio: ingresar el peso y la altura usando "." Ejemplo: altura: 1.66




#EJERCICIO 9:


def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


celsius = float(input("Ingresa la temperatura en grados Celsius: "))
resultado = celsius_a_fahrenheit(celsius)
print(f"{celsius:.2f}°C equivalen a {resultado:.2f}°F")



#EJERCICIO 10



def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio


a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

resultado = calcular_promedio(a, b, c)
print(f"El promedio de los tres números es: {resultado:.2f}")
