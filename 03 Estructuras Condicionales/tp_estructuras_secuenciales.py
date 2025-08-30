# Trabajo Práctico  - Estructuras Secuenciales
# Alumna: Brenda Florencia Romero


# Ejercicio 1

edad = int(input( " Por favor ingrese su edad: "))

if edad > 18:
    print(" Es mayor de edad!")
    
    

# Ejercicio 2

nota = int(input(" Ingrese su nota: "))

if nota >= 6:
    print ("Aprobado")
else:
    print("Desaprobado")
    
    
    
# Ejercicio 3

numero = int(input(" Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
    



# Ejercicio 4

    
    Edad = int(input("Ingrese su edad: "))
    
    if edad < 12:
        print ("Niño/a")
        
    elif edad >= 12 and edad < 18:
        print("Adolescente")
    
    elif edad >= 18 and edad < 30:
        print ("Adulto/a joven")
        
    else:
         print("Adulto/a")
    




# Ejercicio 5
        
contraseña = input("Ingresá una contraseña: ")  
      
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print ("Su contraseña es correcta. ")

else:
    print (" Por favor ingrese su contraseña correctamente: ")
    
 
 
 
 
 # Ejercicio 6: 
 
 
import random
from statistics import mean, median, mode


numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
elif media == mediana == moda:
    sesgo = "Sin sesgo"
else:
    sesgo = "Distribución no claramente sesgada"

print("Lista de números:", numeros_aleatorios)
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print("Resultado:", sesgo)



# Ejercicio 7

 
  
texto = input("Ingrese una frase o palabra: ")

 
if texto[-1].lower() in "aeiou":
    
    texto = texto + "!"
    
print(texto)

 
 
 
 # Ejercicio 8
 
 

nombre = input("Ingrese su nombre: ")

print("Elegí una opción:")
print("1 - Nombre en MAYÚSCULAS")
print("2 - Nombre en minúsculas")
print("3 - Nombre con la primera letra mayúscula")

opcion = input("Ingresá el número de la opción (1, 2 o 3): ")


if opcion == "1":
    nombre_transformado = nombre.upper()
elif opcion == "2":
    nombre_transformado = nombre.lower()
elif opcion == "3":
    nombre_transformado = nombre.title()
else:
    nombre_transformado = "Opción inválida. No se pudo transformar el nombre."


print("Resultado:", nombre_transformado)




# Ejercicio 9


magnitud = float(input("Ingrese la magnitud del terremoto según la escala de Richter:"))

if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud <4:
    categoria = "Leve (ligeramente perceptible)"
elif 4<= magnitud <5:
    categoria = "Moderado (sentido por personas, pero no causa daños)"        
elif 5< magnitud <6:    
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)"
else:
    categoria = "Extremo (puede causar graves daños a gran escala)"
    
        
print("Clasificación:", categoria) 




#Ejercicio 10



hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("Ingresá el mes (1 a 12): "))
dia = int(input("Ingresá el día del mes: "))


fecha = mes * 100 + dia

if hemisferio == "N":
    if 1221 <= fecha <= 320:
        estacion = "Invierno"
    elif 321 <= fecha <= 620:
        estacion = "Primavera"
    elif 621 <= fecha <= 920:
        estacion = "Verano"
    elif 921 <= fecha <= 1220:
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
elif hemisferio == "S":
    if 1221 <= fecha <= 320:
        estacion = "Verano"
    elif 321 <= fecha <= 620:
        estacion = "Otoño"
    elif 621 <= fecha <= 920:
        estacion = "Invierno"
    elif 921 <= fecha <= 1220:
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "Hemisferio inválido"



print("Estación del año:", estacion)

 
 
 
 
 
 
 
