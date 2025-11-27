"""
Crea un programa que me permita saber mi indice de masa corporal (IMC).
y me indique si estoy en un peso saludable, sobrepeso u obesidad.
formula IMC = peso (kg) / (altura (m))^2
"""

# Logica
"""
Entrada:
- input de peso en kg
- input de altura en metros
- definir los rangos de IMC:
Proceso:
- calcular IMC usando la formula
- comparar el IMC con los rangos definidos
Salida:
- mostrar el IMC calculado
"""

# condiciones a tener en cuenta
"""
 1- El peso y la altura no deben ser negativos o cero.
 2- El peso y la altura siempre deben ser numeros.
 3- No se puede ingresar letras o caracteres especiales.
 4- Utilizar el operador logico (AND) que valida que ambas condiciones se cumplan al mismo tiempo.
 5- validar que ambos valores son ingresados.(listo)
"""


lista_mensajes = [
    'Bienvenido al calculador de IMC',
    'No puede ingresar valores negativos o cero',
    'El peso y la altura deben ser numeros validos',
    'No puede ingresar letras o caracteres especiales',
    'Debe llenar ambos campos',
    'El IMC calculado es: ',
    'Intentelo de nuevo',
    ]

print(lista_mensajes[0])
while True:
    peso_usuario = input("Ingrese su peso en kilogramos (kg): ")
    altura_usuario = input("Ingrese su altura en metros (m): ")
    if peso_usuario == '' or altura_usuario == '':
        print(lista_mensajes[4])
        print(lista_mensajes[6])
        continue
    # el usuario ingreso los 2 campos con algun dato
    
    

