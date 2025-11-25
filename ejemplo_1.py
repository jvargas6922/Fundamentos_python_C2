"""
crear un programa que le pida al uusario 6 notas donde hay que mostrar la nota mayor el promedio y ordernar de mayor a menor el total de notas.

Entrada:
    - solicitar al usuario que ingrese 6 notas
Proceso:
    - determinar la nota mayor
    - calcular el promedio de las notas
    - ordenar las notas de mayor a menor

Salida:
    - imprimir la nota mayor
    - imprimir el promedio
    - imprimir las notas ordenadas
"""

# solictar al usuario las notas por medio de un bucle (for).
# notas = []
# for i in range(6):
#     nota = float(input(f"Ingrese la nota {i+1}: "))
#     notas.append(nota)

# # determinar la nota mayor
# # la funcion max() devuelve el valor mayor de una lista
# nota_mayor = max(notas)

# # calcular el promedio de las notas
# # la funcion sum() devuelve la suma de los elementos de una lista
# promedio = sum(notas) / len(notas)

# # ordenar las notas de mayor a menor
# # el metodo sort() ordena la lista en su lugar
# notas.sort(reverse=True)
# # imprimir los resultados
# print(f"La nota mayor es: {nota_mayor}")
# print(f"El promedio de las notas es: {promedio:.2f}")
# print("Las notas ordenadas de mayor a menor son:")
# for nota in notas:
#     print(nota)

#------------------------------------------------------------
# solictar al usuario las notas por medio de un bucle (while).
notas = []
i = 0
while i < 6:
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)
    i += 1

# determinar la nota mayor
nota_mayor = max(notas)

# calcular el promedio de las notas
promedio = sum(notas) / len(notas)

# ordenar las notas de mayor a menor
notas.sort(reverse=True)

# imprimir los resultados
print(f"La nota mayor es: {nota_mayor}")
print(f"El promedio de las notas es: {promedio:.2f}")
print("Las notas ordenadas de mayor a menor son:")
for nota in notas:
    print(nota)