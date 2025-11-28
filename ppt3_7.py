"""
Crea un programa que le permita al usuario poder escojer los productos que desea comprar, debe permitirle agregarlos en un carro temporal y luego debe darle el total de la compra con los descuestos si aplica y el IVA.
"""

#logica
"""
Entrada:
    - Mostrarle a el usuario los productos disponibles con sus precios
    - El usuario debe seleccionar 1 o más productos para agregar al carrito
    - Debemos establer un menu al usuario para poder controlar las acciones que pueda realizar
        * agregar 
        * eliminar 
        * ver
        * pagar
        * salir
Proceso:
    - crear un diccionario con los productos y sus precios
    - crear una lista vacia para el carrito de compras
    - crear un bucle que permita al usuario seleccionar acciones hasta que decida pagar o salir
    - si el usuario selecciona agregar, solicitar el nombre del producto y verificar si existe en el diccionario
    - si existe, agregarlo al carrito
    - si el usuario selecciona eliminar, solicitar el nombre del producto y verificar si existe en el carrito
    - si existe, eliminarlo del carrito
    - si el usuario selecciona ver, mostrar los productos en el carrito y el total parcial
    - si el usuario selecciona pagar, calcular el total con IVA y aplicar descuentos si es necesario
    - mostrar el total final y salir del bucle

Salida:
    - Mostrar detalle de la compra con descuentos e IVA aplicado
"""

productos_disponibles = {
    "manzana":{"precio":1000,"cantidad":1},
    "pancito":{"precio":500,"cantidad":1},
    "leche":{"precio":2500,"cantidad":1},
    "huevo":{"precio":3000,"cantidad":1},
    "carne":{"precio":15000,"cantidad":1},
    "verduras":{"precio":4000,"cantidad":1},
    "helado":{"precio":8000,"cantidad":1}, 
}
carrito_compras = {}
menu = {
    "1": "Agregar producto al carrito",
    "2": "Eliminar producto del carrito",
    "3": "Ver carrito",
    "4": "Pagar",
    "5": "Salir"
}
nombre_cliente = ""
print("\n")
print("*******************************")
print("Bienevenido a la vega virtual")
print("Productos disponibles:")
for producto, info in productos_disponibles.items():
    print(f"|---{producto} => $\033[31m{info['precio']}\033[0m---|")
print("*******************************")
while True:
    nombre_cliente = input("Por favor ingrese su nombre: ")
    if nombre_cliente == "" :
        print("Debe ingresa su nombre por que es obligatorio")
    else:
        break

while True:
    print("\nSeleccione una opción:")
    for clave, valor in menu.items():
        print(f"{clave}. {valor}")
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        producto_a_agregar = input("Ingrese el nombre del producto a agregar: ")
        if producto_a_agregar in productos_disponibles:
            if producto_a_agregar in carrito_compras:
                carrito_compras[producto_a_agregar]["cantidad"] += 1
            else:
                carrito_compras[producto_a_agregar] = {
                    "precio": productos_disponibles[producto_a_agregar]["precio"],
                    "cantidad": 1
                }
            print(f"'{producto_a_agregar}' ha sido agregado al carrito.")
        else:
            print("El producto no está disponible.")

    elif opcion == "2":
        #
        producto_a_eliminar = input("Ingrese el nombre del producto a eliminar: ")
        if producto_a_eliminar in carrito_compras:
            carrito_compras[producto_a_eliminar]["cantidad"] -= 1
            if carrito_compras[producto_a_eliminar]["cantidad"] == 0:
                del carrito_compras[producto_a_eliminar]
            print(f"'{producto_a_eliminar}' ha sido eliminado del carrito.")
        else:
            print("El producto no está en el carrito.")

    elif opcion == "3":
        if carrito_compras:
            print("\nProductos en el carrito:")
            total_parcial = 0
            for producto, info in carrito_compras.items():
                subtotal = info["precio"] * info["cantidad"]
                total_parcial += subtotal
                print(f"- {producto}: ${info['precio']} x {info['cantidad']} = ${subtotal}")
            print(f"Total parcial: ${total_parcial}")
        else:
            print("El carrito está vacío.")

    elif opcion == "4":
        if carrito_compras:
            total_final = 0
            for info in carrito_compras.values():
                total_final += info["precio"] * info["cantidad"]
            iva = total_final * 0.19
            total_con_iva = total_final + iva
            print(f"\nTotal antes de IVA: ${total_final:.0f}")
            print(f"IVA (19%): ${iva:.0f}")
            print(f"Total a pagar: ${total_con_iva:.0f}")

    elif opcion == "5":
        print("Gracias por su compra. ¡Hasta luego!")
        break
    else:
        print("opcin inválida. Por favor, seleccione una opción válida.")