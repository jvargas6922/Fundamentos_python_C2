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
 1- El peso y la altura no deben ser negativos o cero. (listo)
 2- El peso y la altura siempre deben ser numeros.
 3- No se puede ingresar letras o caracteres especiales. (listo)
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
        print(lista_mensajes[4]) # Debe llenar ambos campos
        print("------------------")
        print(lista_mensajes[6]) # Intentelo de nuevo
        print("------------------")
        continue
    # el usuario ingreso los 2 campos con algun dato
    # validamos que los campos no sean caracteres, valores negativos o cero.
    elif not peso_usuario.replace('.','',1).isdigit() or not altura_usuario.replace('.','',1).isdigit() or float(peso_usuario) <= 0 or float(altura_usuario) <= 0:
        print(lista_mensajes[2]) # El peso y la altura deben ser numeros validos
        print("------------------")
        print(lista_mensajes[6]) # Intentelo de nuevo
        print("------------------")
        continue
    else:
        # ambos campos contienen los valores esperados
        peso_usuario = float(peso_usuario)
        altura_usuario = float(altura_usuario)
        break

# Calculo del IMC
imc = peso_usuario / (altura_usuario ** 2)
print(f"{lista_mensajes[5]} {imc:.2f}")

# Evaluacion del IMC
if imc < 18.5:
    print("Estas por debajo del peso saludable.")
elif 18.5 <= imc < 24.9:
    print("Estas en un peso saludable.")
elif 25 <= imc < 29.9:
    print("Tienes sobrepeso.")
else:
    print("Tienes obesidad.")
    
    

