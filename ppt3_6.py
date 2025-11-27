"""
Contexto: 🙌
Una tienda de electrónicos necesita un sistema que ayude a clasificar los productos según su
disponibilidad y tipo. Dependiendo de si un producto está en stock o no, y de la categoría a la que
pertenece (electrodoméstico, teléfono, computadora, accesorio, etc.), el sistema debe proporcionar
información adecuada al cliente.
Consigna: ✍
Crear un código en python que:
➜ Determine si un producto está en stock o agotado.
➜ Si está en stock, identifique a qué categoría pertenece y muestre un mensaje adecuado.
➜ Si el producto no está en la lista de categorías predefinidas, indicar que no se tiene información
disponible.
"""

# Razonamiento de posibles casuísticas:
"""
    - 1 El producto existe en la tienda
    - 2 El producto tiene stock
    - 3 Mostrar los datos del productos(categoría, disponibilidad, descripcion) en caso de no tener categoria agregamos S/I
"""

"""
Entrada:
    - Establer el diccionario de productos
    - Socilicita al usuario el nombre del producto a consultar
Proceso:
    - Verificar si el producto existe en el diccionario
    - Si existe, verificar si está en stock
    - Si está en stock, mostrar la categoría y un mensaje adecuado
    - Si no está en stock, informar que está agotado
    - Si no existe, informar que no se tiene información disponible (esta de más)
Salida:
    - Mensaje indicando la disponibilidad y categoría del producto
"""

productos_tienda = {
    "Televisor Samsung": {"categoria": "Electrodoméstico", "stock": True},
    "iPhone 13": {"categoria": "Teléfono", "stock": False},
    "Laptop Dell": {"categoria": "Computadora", "stock": True},
    "Auriculares Sony": {"categoria": "Accesorio", "stock": True},
    "Refrigerador LG": {"categoria": "Electrodoméstico", "stock": False},
    "Dron": {"categoria": "S/I", "stock": False},
}
#print(productos_tienda)
while True:
    producto_consultado = input("Ingrese el nombre del producto a consultar: ")
    # valido que el producto consultado por el usuario existe en mi productos de la tienda
    if producto_consultado in productos_tienda:
        # obtengo la info del producto
        producto_info = productos_tienda[producto_consultado]
        if producto_info["stock"]:
            print(f"El producto '{producto_consultado}' está en stock.")
            print(f"Categoría: {producto_info['categoria']}")
        else:
            print(f"El producto '{producto_consultado}' está agotado.")
            print(f"Categoría: {producto_info['categoria']}")

        break
    else:
        print("No se tiene información disponible sobre ese producto o no exiete en la tienda.")