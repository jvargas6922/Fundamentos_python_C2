"""
Validacion simple de condicionales
"""

# Ejemplo 1

# edad = int(input("Ingrese su edad: "))

# opcion 1:
# if edad >= 18:
#     print("Eres mayor de edad.")
# else:
#     print("Eres menor de edad.")

# opcion 2:
# if edad < 18:
#     print("Eres menor de edad.")
# else:
#     print("Eres mayor de edad.")

"""
# Ejemplo 2
¿En qué consistirá la Demo?
Tenemos un sistema de reservas de un cine. Dependiendo del tipo de usuario (cliente regular,
estudiante, jubilado, etc.), el sistema debe aplicar un descuento diferente en la compra del boleto.
Si el tipo de usuario no está en la lista, el precio se mantiene normal.
1. ¿Cuántas condiciones debemos evaluar en este problema?
2. ¿Qué estructura condicional nos ayudaría a organizarlo mejor?
3. ¿Cómo evitar repetir código innecesario?
4. ¿Qué pasaría si el usuario ingresa un tipo no reconocido?
"""

# Logica
"""
Entrada:
 - pedir el tipo de usuario
 - valor del boleto
 - descuento por tipo de usuario
Proceso:
    - Calculo del descuento segun el tipo de usuario
    - Aplicacion del descuento al valor del boleto
    - Validar el tipo de usuario ()
Salida:
    - Mostrar el valor final del boleto
"""
valor_boleto = 7000
tipo_usuarios =["cliente regular", "estudiante", "jubilado"]
descuentos = [10, 20, 40]

# lower() => convierte a minusculas
tipo_usuario = input("Ingrese su tipo de usuario (\ncliente regular, \nestudiante, \njubilado): ").lower()
if tipo_usuario in tipo_usuarios:
    indice = tipo_usuarios.index(tipo_usuario)
    descuento = descuentos[indice]
    valor_final = valor_boleto - (valor_boleto * descuento / 100)
    print(f"El valor final del boleto con un descuento del {descuento}% es: {valor_final}")
else:
    print(f"Tipo de usuario normal. El valor del boleto es: {valor_boleto}")
