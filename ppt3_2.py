"""
Aplicar un condicional simple (if) para detectar si un vehículo supera el límite de velocidad
permitido.
Vamos a imaginar que estamos diseñando un sistema que detecta si un conductor excede
la velocidad máxima permitida en una zona. Si supera los 60 km/h, el sistema debe
advertirlo
Lo primero que haremos es pedirle al usuario que ingrese su velocidad actual. Como es un
número con decimales, lo convertiremos a float.
Luego usaremos una estructura if para verificar si la velocidad ingresada es mayor a 60. Si
lo es, mostraremos un mensaje de advertencia.
"""

# logica
"""
Entrada:
    - pedirle al usuario la velocidad actual
Proceso:
    - validar si la velocidad supera el limite permitido
Salida:
    - mostrar mensaje de advertencia si se supera el limite
"""
# las veces que voy a controlar al usuario
import time
monitoreo = 10

lista_velocidades = []
for i in range(monitoreo):
    #solicito la velocidad actual
    velocidad_actual = float(input("Ingrese su velocidad actual (km/h): "))
    lista_velocidades.append(velocidad_actual)
    # espero 5s antes de la siguiente lectura
    #time.sleep(5) #simula el tiempo entre lecturas

for velocidad in lista_velocidades:
    if velocidad >= 60:
        print(f"Advertencia: Ha excedido el límite de velocidad permitido! (Velocidad actual: {velocidad} km/h)")
    else:
        time.sleep(5)
        print(f"Velocidad dentro del límite permitido. (Velocidad actual: {velocidad} km/h)")