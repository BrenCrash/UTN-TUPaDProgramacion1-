# Práctico 6: Estructuras de datos complejas 
#Alumna: Brenda Florencia Romero




# EJERCICIO 1: 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}


precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)


# EJERCICIO 2: 


precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)


# EJERCICIO 3:


frutas = list(precios_frutas.keys())

print(frutas)


# EJERCICIO 4: 



contactos = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    contactos[nombre] = numero


consulta = input("Ingrese el nombre que desea buscar: ")

if consulta in contactos:
    print(f"El número de {consulta} es {contactos[consulta]}")
else:
    print("Ese contacto no existe en la agenda.")



# EJERCICIO 5:


frase = input("Escribí una frase: ")


palabras = frase.split()
palabras_unicas = set(palabras)


recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1


print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)



# EJERCICIO 6: 


alumnos = {}


for i in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(map(int, input("Ingresa 3 notas separadas por espacio: ").split()))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: notas {notas} -> promedio {promedio:.2f}")
    
    

# EJERCICIO 7: 


parcial1 = {"Sofía", "Juan", "Lucía", "Marcos"}
parcial2 = {"Lucía", "Pedro", "Marcos", "Ana"}


ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2


print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)


# EJERCICIO 8: 


stock = {
    "manzanas": 10,
    "bananas": 5,
    "naranjas": 8
}


print("Productos disponibles:", stock)


producto = input("Ingresa el nombre del producto que querés consultar: ").lower()

if producto in stock:
    print(f"El stock actual de {producto} es {stock[producto]} unidades.")
    
    agregar = input("¿Querés agregar más unidades? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock[producto]} unidades.")
else:
    print("Ese producto no existe en el inventario.")
    
    nuevo = input("¿Querés agregarlo al inventario? (s/n): ").lower()
    if nuevo == "s":
        cantidad = int(input("¿Cuántas unidades iniciales tiene?: "))
        stock[producto] = cantidad
        print(f"Se agregó el producto '{producto}' con {cantidad} unidades.")


print("\nInventario actualizado:")
print(stock)



# EJERCICIO 9: 


agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "18:30"): "Gimnasio"
}

print("Agenda actual:")
for clave, evento in agenda.items():
    print(f"{clave[0].capitalize()} a las {clave[1]} → {evento}")


dia = input("\nIngresá el día que querés consultar: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")


if (dia, hora) in agenda:
    print(f"\nActividad para el {dia} a las {hora}: {agenda[(dia, hora)]}")
else:
    print(f"\nNo hay actividad registrada para el {dia} a las {hora}.")



# EJERCICIO 10:



paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia"
}


invertido = {capital: pais for pais, capital in paises.items()}

print("Diccionario original:", paises)
print("Diccionario invertido:", invertido)



































