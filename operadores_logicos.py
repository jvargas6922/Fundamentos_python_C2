# Operadores lógicos en Python
"""
operador AND
operador OR
operador NOT
conbinación de operadores lógicos
"""
# Ejemplos de uso de operadores lógicos
# a = True
# b = False
# # Operador AND
# resultado_and = a and b  # False
# print("Resultado de AND:", resultado_and)
# # Operador OR
# resultado_or = a or b    # True
# print("Resultado de OR:", resultado_or)
# # Operador NOT
# resultado_not = not a    # False
# print("Resultado de NOT:", resultado_not)
# # Combinación de operadores lógicos
# resultado_combinado = (a and b) or (not b)  # True
# #.                      False       True
# # Imprimir el resultado combinado   
# print("Resultado combinado:", resultado_combinado)

# Ejemplo con operadores logicos.
"""
crea un programa que me permita verificar si las creadenciales ingresadas por el usuario son correctas

Entrada:
    Solicitar al usuario que ingresas sus credenciales (usuario y contraseña).
Proceso:
    validar si el usuario y la contraseña son correctos utilizando operadores lógicos.
    usuario correcto: "admin"
    contraseña correcta: "1234"
Salida:
    Mostrar un mensaje indicando si las credenciales son correctas o incorrectas.
"""

# credenciales correctas
usuario_correcto = "admin"
contraseña_correcta = "1234"

usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: ")

# while True:
#     if (usuario == usuario_correcto) and (contraseña == contraseña_correcta):
#         print("Credenciales correctas. Acceso concedido.")
#         break # salir del bucle
#     else:
#         print("Credenciales incorrectas. Intente de nuevo.")
#         usuario = input("Ingrese su usuario: ")
#         contraseña = input("Ingrese su contraseña: ")

intentos = 5
while intentos > 0:
    if (usuario == usuario_correcto) and (contraseña == contraseña_correcta):
        print("Credenciales correctas. Acceso concedido.")
        break # salir del bucle
    else:
        intentos -= 1
        print(f"Credenciales incorrectas. Te quedan {intentos} intentos.")
        if intentos == 0:
            print("Has agotado todos los intentos. Acceso denegado.")
            break
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")