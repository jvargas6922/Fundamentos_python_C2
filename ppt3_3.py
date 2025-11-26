"""
Un programa debe clasificar la calificación de un
estudiante según su puntaje:
● 90 o más: Excelente
● 80-89: Muy bueno
● 70-79: Bueno
● Menos de 70: Necesita mejorar
Explicación:
● Se solicita al usuario que ingrese su puntaje.
● Se evalúan las condiciones en orden
● Se garantiza que solo una de las condiciones se
ejecuta.
● Se utiliza else como opción por defecto.
"""

"""
Entrada:
    - definir los rangos de calificación
    - solicitar al usuario su puntaje
Proceso:
    - evaluar en que rango se encuenta el puntaje del usuario
Salida:
    - mostrar la calificación correspondiente
"""

print("La calificacion que se esta solicitando es desde 0 hasta 100")
while True:
    calificacion_usuario = input("Ingrese su puntaje: ")
    # validar que el uuario no ingrese un texto, pero validar que sea datos numerico
    if not calificacion_usuario.isdigit():
        print("No se permiten textos, intente de nuevo")
        # continue
        # el usuario ingreso un numero pero no se si es float o int
        # print("llegue aqui")
        # print(type(calificacion_usuario))
        # print("Debe ingresar un numero entero, intente de nuevo")
    elif '.' in calificacion_usuario:
         print("Debe ingresar un numero entero, intente de nuevo")
    else:
        print(type(calificacion_usuario))
        calificacion_usuario = int(calificacion_usuario)
        if calificacion_usuario > 100 or calificacion_usuario <= 0:
            print("El puntaje incorrecto, intente de nuevo") 
        else:
            break

if calificacion_usuario >= 90:
    print("Excelente")
elif (calificacion_usuario >= 80) and (calificacion_usuario <= 89):
    print("Muy bueno")
elif (calificacion_usuario >= 70) and (calificacion_usuario <= 79):
    print("Bueno")
else:
    print("Necesita mejorar")