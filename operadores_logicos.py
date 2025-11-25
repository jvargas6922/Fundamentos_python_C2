# Operadores lógicos en Python
"""
operador AND
operador OR
operador NOT
conbinación de operadores lógicos
"""
# Ejemplos de uso de operadores lógicos
a = True
b = False
# Operador AND
resultado_and = a and b  # False
print("Resultado de AND:", resultado_and)
# Operador OR
resultado_or = a or b    # True
print("Resultado de OR:", resultado_or)
# Operador NOT
resultado_not = not a    # False
print("Resultado de NOT:", resultado_not)
# Combinación de operadores lógicos
resultado_combinado = (a and b) or (not b)  # True
#.                      False       True
# Imprimir el resultado combinado   
print("Resultado combinado:", resultado_combinado)