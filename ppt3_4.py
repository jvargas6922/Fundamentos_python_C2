"""
¿En qué consistirá la Demo?
Tenemos un sistema de recomendación de vestimenta según la temperatura del día. Dependiendo de la
temperatura ingresada por el usuario, el programa sugiere qué tipo de ropa usar:
➜
🥶Menos de 10°C → Abrigo grueso y bufanda
➜
󰷻Entre 10°C y 20°C → Chaqueta ligera
➜
😎Entre 21°C y 30°C → Ropa cómoda y fresca
➜
🥵Más de 30°C → Ropa ligera y protector solar
Si el usuario ingresa un valor fuera de rango o no numérico, el sistema deberá indicar un mensaje de error.
"""

#logica
"""
Entrada:
    - definir los rangos de las temperaturas
    - solicitar al usuario su temperatura
Proceso:
    - evaluar en que rango se encuenta la temperatura del usuario
Salida:
    - mostrar la recomendación correspondiente
"""
print("Tenemos un sistema de recomendación de vestimenta según la temperatura del día. \nDependiendo de la temperatura ingresada por el usuario,\nel programa sugiere qué tipo de ropa usar:")

while True:
    temperatura_usuario = input("Ingrese la temperatura del día en °C: ")
    # necesito validar que el usuario no ingreso cadena de texto
    if not temperatura_usuario.replace('.','',1).isdigit():
        print("No se permiten textos, intente de nuevo")
        print("Error: Entrada no válida")
    else:
        temperatura_usuario = float(temperatura_usuario)
        break

if temperatura_usuario < 10:
    print("🥶 Menos de 10°C → Abrigo grueso y bufanda")
elif 10 <= temperatura_usuario <= 20:
    print("Entre 10°C y 20°C → Chaqueta ligera")
elif 21 <= temperatura_usuario <= 30:
    print("😎 Entre 21°C y 30°C → Ropa cómoda y fresca")
else:
    print("🥵 Más de 30°C → Ropa ligera y protector solar")

