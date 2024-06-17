import json
import os

def guardar_diccionario(diccionario, archivo="lista_compra.json"):
    # Guarda el diccionario en un archivo JSON antes de salir
    with open(archivo, "w") as f:
        json.dump(diccionario, f, indent=4)
    print(f"Datos guardados en {archivo}")

def crear_archivo():
    with open("lista_compra.json", "w") as f:
        print("Archivo 'lista_compra.json' creado\n")

def añadir_producto(diccionario):
    producto = input("Nombre del producto: ")
    cantidad = input("Cantidad: ")
    diccionario[producto] = cantidad
    print(f"Producto '{producto}' añadido.")

def listar_productos(diccionario):
    if not diccionario:
        print("No hay productos en la lista de la compra.")
    else:
        for producto, cantidad in diccionario.items():
            print(f"Producto: {producto}, Cantidad: {cantidad}")

def eliminar_producto(diccionario):
    producto = input("Nombre del producto a eliminar: ")
    if producto in diccionario:
        del diccionario[producto]
        print(f"Producto '{producto}' eliminado.")
    else:
        print("Producto no encontrado.")

def modificar_producto(diccionario):
    producto = input("Nombre del producto a modificar: ")
    if producto in diccionario:
        cantidad = input("Nueva cantidad: ")
        diccionario[producto] = cantidad
        print(f"Producto '{producto}' modificado.")
    else:
        print("Producto no encontrado.")

def mostrar_menu():
    print("""
    Menú Lista de la Compra:
    1. Añadir producto a la lista
    2. Listar productos de la lista
    3. Eliminar un producto de la lista
    4. Modificar un producto de la lista
    5. Salir
    """)
    return int(input("Elige una opción: "))

def gestionar_lista_compra():
    archivo = "lista_compra.json"
    diccionario = {}
    
    # Si existe el archivo, lo leemos y guardamos en el diccionario
    if os.path.isfile(archivo):
        with open(archivo, "r") as f:
            diccionario = json.load(f)
    else:
        crear_archivo()
    
    opcion = 0
    while opcion != 5:
        opcion = mostrar_menu()
        if opcion == 1:
            añadir_producto(diccionario)
        elif opcion == 2:
            listar_productos(diccionario)
        elif opcion == 3:
            eliminar_producto(diccionario)
        elif opcion == 4:
            modificar_producto(diccionario)
        elif opcion == 5:
            guardar_diccionario(diccionario, archivo)
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Por favor, elige nuevamente.")

# Ejecutar el programa
def pex2(): 
    gestionar_lista_compra()