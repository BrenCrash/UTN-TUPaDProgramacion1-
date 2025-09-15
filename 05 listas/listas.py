# Trabajo Práctico – Listas
# Alumna: Brenda Florencia Romero 


# Ejercicio 1:


notas = [ 7.5, 8.0, 5.5, 6.5, 9.1, 5.5, 10.0, 4.8, 6.9, 8.7,]

print ("Notas de los estudiantes", notas )
promedio = sum(notas) / len(notas)

print ("Promedio de notas: ", promedio)


nota_max = max(notas)
nota_min = min(notas)

print ("Notas mas alta:" , nota_max )
print ("Nota mas baja: ", nota_min)



# Ejercicio 2:

productos = []

for i in range(5):
    producto = input(f"Ingrese el producto {i+1}:")
    productos.append(producto)

    
    
print ("Lista original", productos)
    
 
productos_ordenados = sorted(productos)
print("Lista ordenada alfábeticamente: ", productos_ordenados)

 
Eliminar = input("Ingrese el producto que desea eliminar: ")
 
 
if Eliminar in productos_ordenados:
    productos_ordenados.remove(Eliminar)
    print ("Lista actualizada: ", productos_ordenados)
else:
    print("El producto no se encuentra en la lista.")
    
    

 
 
 # Ejercicio 3:
 
 
import random
 
numeros = []

for i in range(15):
    numeros.append(random.randint(1, 100))
    
 
print("Lista de números generados: ", numeros)
 
pares = []
impares = []


for n in numeros:
    if n % 2 == 0:   
        pares.append(n)
    else:            
        impares.append(n)

        

print("Números pares:", pares)
print("Cantidad de pares:", len(pares))

print("Números impares:", impares)
print("Cantidad de impares:", len(impares)) 
 
 
 
# Ejercicio 4

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

sin_repetidos = list(set(datos))

print("Lista original:", datos)
print("Lista sin repetidos:", sin_repetidos)

    
 
 




 # Ejercicio 5: 
 

estudiantes = ["Brenda", "Melisa", "Sofia", "Sara", "Abril", "Kevin", "Pablo", "Daniela"]

print("Lista inicial de estudiantes:")
print(estudiantes)

opcion = input("¿Queres agregar o eliminar un estudiante? Escribí 'agregar' o 'eliminar': ")

if opcion == "agregar":
    nuevo = input("Ingresá el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print(f"El estudiante {nuevo} fue agregado correctamente.")

elif opcion == "eliminar":
    borrar = input("Ingresá el nombre del estudiante que desea eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)
        print(f"El estudiante {borrar} fue eliminado correctamente.")
    else:
        print("El estudiante indicado no se encuentra en la lista.")

else:
    print("La opción ingresada no es válida. No se realizaron cambios.")

print("\nLista final de estudiantes:")
print(estudiantes)

    
# Ejercicio 6:


#Numeros que usé de ejemplo 
numeros = [10, 20, 30, 40, 50, 60, 70]

print("Lista original:")
print(numeros)


ultimo = numeros[-1]


rotada = [ultimo] + numeros[:-1]

print("\nLista rotada hacia la derecha:")
print(rotada)

    
    
# Ejercicio 7:   



temperaturas = [
    [12, 25],  # Dia 1
    [14, 28],  # Dia 2
    [11, 22],  # Dia 3
    [15, 30],  # Dia 4
    [13, 27],  # Dia 5
    [10, 20],  # Dia 6
    [16, 32]   # Dia 7
]


minimas = [dia[0] for dia in temperaturas]  # todas las mínimas
maximas = [dia[1] for dia in temperaturas]  # todas las máximas

prom_min = sum(minimas) / len(minimas)
prom_max = sum(maximas) / len(maximas)

amplitudes = [dia[1] - dia[0] for dia in temperaturas]
dia_mayor_amplitud = amplitudes.index(max(amplitudes)) + 1


print(f"Promedio de temperaturas mínimas: {prom_min:.2f}°C")
print(f"Promedio de temperaturas máximas: {prom_max:.2f}°C")
print(f"El día con mayor amplitud térmica fue el Día {dia_mayor_amplitud} con {max(amplitudes)}°C de diferencia.")

    
    
# Ejercicio 8:


notas = [
    [7, 8, 6],   # Estudiante 1
    [5, 9, 7],   # Estudiante 2
    [8, 6, 9],   # Estudiante 3
    [6, 7, 5],   # Estudiante 4
    [9, 8, 10]   # Estudiante 5
]

print("Promedio de cada estudiante:")
for i, fila in enumerate(notas, start=1):
    promedio_estudiante = sum(fila) / len(fila)
  
    print(f"Estudiante {i}: {promedio_estudiante:.2f}")


print("\nPromedio de cada materia:")
materias = len(notas[0])  
for j in range(materias):
    columna = [notas[i][j] for i in range(len(notas))] 
    promedio_materia = sum(columna) / len(columna)
   
    print(f"Materia {j+1}: {promedio_materia:.2f}")





# Ejercicio 9:


tablero = [["-" for _ in range(3)] for _ in range(3)] #Recordar tablero

def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))
    print()


print("Tablero inicial:")
mostrar_tablero()


 
for turno in range(2):  
    if turno % 2 == 0:
        jugador = "X"
    else:
        jugador = "O"
    
    print(f"Turno del jugador {jugador}")
    fila = int(input("Ingresá la fila (0, 1 o 2): "))
    columna = int(input("Ingresá la columna (0, 1 o 2): "))

     
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("Esa casilla ya está ocupada. Perdés el turno.")

    mostrar_tablero()





# Ejercicio 10:


ventas = [
    [5, 7, 6, 4, 3, 8, 6],   # Producto 1
    [3, 5, 4, 6, 7, 5, 4],   # Producto 2
    [8, 6, 7, 5, 6, 7, 9],   # Producto 3
    [2, 4, 3, 5, 4, 6, 5]    # Producto 4
]


print("Total vendido por cada producto:")
totales_productos = []
for i, fila in enumerate(ventas, start=1):
    total = sum(fila)
    totales_productos.append(total)
    print(f"Producto {i}: {total}")


totales_dias = [sum(columna) for columna in zip(*ventas)]

dia_max = totales_dias.index(max(totales_dias)) + 1
print(f"\nEl día con mayores ventas totales fue el Día {dia_max} con {max(totales_dias)} ventas.")


producto_max = totales_productos.index(max(totales_productos)) + 1
print(f"El producto más vendido en la semana fue el Producto {producto_max} con {max(totales_productos)} ventas.")





















    
    
    
    
    
    
    