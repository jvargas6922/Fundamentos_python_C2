# nuestra variable promedio tiene el valor de 7
promedio = 7
#-------------
nota_1 = 5
nota_2 = 3
suma = nota_1 + nota_2
#-------------
promedio = suma / 2
# print("El promedio es:", promedio)

# Tipo de datos en python
# nombre = "Joffred"
# print(type(nombre))
# numero = 10
# print(type(numero))
# correr = True
# print(type(correr))
# lista_objetos = ["libro", "lapiz", "cuaderno"]
# print(type(lista_objetos))

# variables de tipo entero
# 1- tipo de variables entero.
"""
    crea un programa que me permita saber cual de las 2 edades ingresadas es la mayor
Entrada:
    - solicitar al usuario que ingrese las 2 edades
Proceso:
    - comparar las 2 edades y determinar cual es la mayor
Salida:
    - imprimir en pantalla cual de las 2 edades es la mayor
"""
# edad_1 = int(input("Ingrese la primera edad: "))
# edad_2 = int(input("Ingrese la segunda edad: "))

# # tenemos las edades ingresadas por el usuario.
# if edad_1 > edad_2:
#     print("La primera edad es mayor:", edad_1)
# elif edad_2 > edad_1:
#     print("La segunda edad es mayor:", edad_2)
# else:
#     print("Ambas edades son iguales:", edad_1)

# print("Fin del programa")

# variable de tipo cadena.
"""
    Crea un programa que me permita saludar al usuario que se esta registrando en un sitio web.

    Entrada:
        - Solicitar al usuario que ingrese sus datos
    Proceso:
        - Almacenar los datos en un variables
    Salida:
        - Imprimir el mensaje de bienvenida con el nombre del usuario
""" 

# nombre_usuario = input("Ingrese su nombre de usuario: ")
# apellido_usuario = input("Ingrese su apellido de usuario: ")
# mensaje = f"Bienvenido al sitio Web  {nombre_usuario} {apellido_usuario} es un placer tenerlo"
# print(mensaje)

# variables de tipo decimal o flotante
"""
crea un programa que me permita calcular el precio de un producto con descuento.
Entrada:
    - solicitar al usuario que ingrese el precio del producto y el porcentaje de descuento
Proceso:
    - calcular el precio con descuento
Salida:
    - imprimir en pantalla el precio con descuento
"""

# precio_producto = float(input("Ingrese el precio del producto: "))
# porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

# descuento = (porcentaje_descuento / 100) * precio_producto
# precio_con_descuento = precio_producto - descuento
# print("El precio con descuento es:", precio_con_descuento)

# variables de tipo booleano
"""
Crea un programa que me permita determinar si un numero es par o impar.
Entrada:
    - solicitar al usuario que ingrese un numero entero
Proceso:
    - determinar si el numero es par o impar
Salida:
    - imprimir en pantalla si el numero es par o impar

"""
# numero_entero = int(input("Ingrese un numero entero: "))
# if numero_entero % 2 == 0: # True
#     print("El numero es par" , True)
# else:# False
#     print("El numero es impar" , False)

# variables de tipo lista
"""
Crea un programa que me permita almacenar una lista de compras y mostrarla al usuario.

Entrada:
    - solicitar al usuario que ingrese los productos de la lista de compras
Proceso:
    - almacenar los productos en una lista
Salida:
    - imprimir en pantalla la lista de compras
"""
# lista_compras = []

# producto_1 = input("Ingrese el primer producto de la lista de compras: ")
# lista_compras.append(producto_1)
# producto_2 = input("Ingrese el segundo producto de la lista de compras: ")
# lista_compras.append(producto_2)
# producto_3 = input("Ingrese el tercer producto de la lista de compras: ")
# lista_compras.append(producto_3)

# print("Lista de compras:", lista_compras)

# variables de tipo diccionario
"""
crea un programa que me permita registrar los datos de un vehiculo.

Entrada:
    - solicitar al usuario que ingrese los datos del vehiculo
    - solicitar al usuario que ingrese la marca, modelo y año del vehiculo
Proceso:
    - almacenar los datos en un diccionario
Salida:
    - imprimir en pantalla los datos del vehiculo
"""
vehiculo = {}
marca = input("Ingrese la marca del vehiculo: ")
modelo = input("Ingrese el modelo del vehiculo: ")
anio = input("Ingrese el año del vehiculo: ")

vehiculo["marca"] = marca
vehiculo["modelo"] = modelo
vehiculo["anio"] = anio

print("Datos del vehiculo:", vehiculo)