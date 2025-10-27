# Trabajo práctico de Recursividad  
# Alumna: Brenda FLorencia Romero


# EJERCICIO 1:


def factorial(n):

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingresa un número entero: "))
for i in range(1, numero + 1):
    print(f"El factorial de {i} es {factorial(i)}")



# EJERCICIO2:

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        
        return fibonacci(n - 1) + fibonacci(n - 2)


posicion = int(input("Ingresa la cantidad de términos que deseas ver de la serie: "))

print(f"\nSerie de Fibonacci hasta la posición {posicion}:")
for i in range(posicion):
    print(fibonacci(i), end="  ")



# EJERCICIO 3:

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
    
        return base * potencia(base, exponente - 1)


base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))


resultado = potencia(base, exponente)
print(f"\n{base} elevado a la {exponente} es igual a {resultado}")



# EJERCICIO 4:


def decimal_a_binario(n):
    
    if n < 2:
        return str(n)
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


numero = int(input("Ingresa un número entero positivo: "))
binario = decimal_a_binario(numero)
print(f"\nEl número {numero} en binario es: {binario}")


# EJERCICIO 5:

def es_palindromo(palabra):
     
    if len(palabra) <= 1:
        return True
     
    elif palabra[0] != palabra[-1]:
        return False
    else:
         
        return es_palindromo(palabra[1:-1])

 
texto = input("Ingresa una palabra (sin espacios ni tildes): ").lower()

resultado = es_palindromo(texto)

if resultado:
    print(f"'{texto}' es un palíndromo.")
else:
    print(f"'{texto}' no es un palíndromo.")



# EJERCICIO 6: 

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)


numero = int(input("Ingresa un número entero positivo: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")



# EJERCICIO 7:

def contar_bloques(n):
    
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


nivel = int(input("Ingresa la cantidad de bloques en el nivel más bajo: "))
total = contar_bloques(nivel)
print(f"Para construir una pirámide con {nivel} bloques en el nivel inferior se necesitan {total} bloques en total.")



# EJERCICIO 8:

def contar_digito(numero, digito):
    
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    else:
        
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)


numero = int(input("Ingresa un número entero positivo: "))
digito = int(input("Ingresa el dígito que deseas contar (0-9): "))

cantidad = contar_digito(numero, digito)
print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")


