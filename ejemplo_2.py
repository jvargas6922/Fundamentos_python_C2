"""
Desarrolla un programa en python que te permita simular las operaciones de un cajero automatico.
Acciones a tener en cuenta:
- consultar saldo
- ingresar dinero
- retirar dinero
- saldo inicial sera de 1000 dolares
- el cajero no debe permitir retirar mas dinero del que hay en la cuenta
- Al finalizar la ejecucion me debe indicar si deseo hacer otra operacion o salir

Entrada:
 ingresar el monto inicial: 1000
 el usuario debe ingresar las credenciales correctas para ingresar al cajero en caso contrario tendra solo 3 intentos
Proceso:
    - mostrar menu de opciones
    - ejecutar la operacion seleccionada
Salida
    - mostrar el saldo actual
    - mostrar mensaje de error en caso de que se intente retirar mas dinero del que hay en la cuenta
"""
saldo  = 1000
intentos = 3
usuario_correcto = "admin"
contrasena_correcta = "12345"

lista_opciones = [
    "1. Consultar saldo", 
    "2. Ingresar dinero", 
    "3. Retirar dinero", 
    "4. Salir"
]

for intento in range(intentos):
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contrasena: ")
    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        print("Acceso concedido.")
        while True:
            print("\nMenu de opciones:")
            for opcion in lista_opciones:
                print(opcion)
            eleccion = input("Seleccione una opcion (1-4): ")
            if eleccion == "1":
                print(f"Su saldo actual es: ${saldo}")
            elif eleccion == "2":
                monto_ingreso = float(input("Ingrese el monto a depositar: $"))
                if monto_ingreso > 0:
                    saldo += monto_ingreso
                    print(f"Has ingresado ${monto_ingreso}. Nuevo saldo: ${saldo}")
                else:
                    print("El monto a ingresar debe ser positivo.")
            elif eleccion == "3":
                # opciones de retiros con multiplos de 5 
                monto_retiro = float(input("Ingrese el monto a retirar: $"))
                if monto_retiro > saldo:
                    print("Error: No puede retirar mas dinero del que hay en la cuenta.")
                elif monto_retiro <= 0:
                    print("El monto a retirar debe ser positivo.")
                else:
                    saldo -= monto_retiro
                    print(f"Has retirado ${monto_retiro}. Nuevo saldo: ${saldo}")
            elif eleccion == "4":
                print("Gracias por usar el cajero automatico. Hasta luego!")
                break
            else:
                print("Opcion no valida. Por favor seleccione una opcion del 1 al 4.")
        break
    else:
        if intento == intentos - 1:
            print("Ha excedido el numero de intentos. Acceso denegado.")
            exit()
        else:
            print(f"Credenciales incorrectas. Le quedan {intentos - intento - 1} intentos.")