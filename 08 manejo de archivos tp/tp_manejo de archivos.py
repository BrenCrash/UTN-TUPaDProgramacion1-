 
 #Archivos - Práctica
 # Alumna: Brenda Florencia Romero
 
 # EJERCICIO 1:
 
productos = [
    "Lapicera,150,20\n",
    "Cuaderno,500,10\n",
    "Regla,100,15\n"
]

with open("productos.txt", "w") as archivo:
    archivo.writelines(productos)

print("Archivo 'productos.txt' creado correctamente.")


# EJERCICIO 2:


with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    nombre, precio, cantidad = linea.strip().split(",")
    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


# EJERCICIO 3:


with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()

print("=== LISTA DE PRODUCTOS ===")
for linea in lineas:
    nombre, precio, cantidad = linea.strip().split(",")
    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


print("\n=== AGREGAR NUEVO PRODUCTO ===")
nombre = input("Nombre del producto: ")
precio = input("Precio: ")
cantidad = input("Cantidad: ")

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print("\n Producto agregado correctamente al archivo.")


# EJERCICIO 4:

productos = []  


with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        
        productos.append(producto)

print("=== LISTA DE PRODUCTOS ===")
for p in productos:
    print(p)



# EJERCICIO 5:

productos = []  
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)


nombre_buscar = input("Ingresa el nombre del producto a buscar: ").strip()
encontrado = False
for p in productos:
    if p["nombre"].lower() == nombre_buscar.lower():
        print("Producto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("El producto no existe en la lista.")




# EJERCICIO 6:

productos = []
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)


print("Lista de productos actual:")
for p in productos:
    print(f"{p['nombre']} - ${p['precio']} - Cantidad: {p['cantidad']}")


with open("productos.txt", "w") as archivo:
    for p in productos:
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea)

print("Archivo 'productos.txt' sobrescrito correctamente con los productos actualizados.")





