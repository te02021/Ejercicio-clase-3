"""
Desarrolle un algoritmo para determinar si un año leído por teclado es o no bisiesto. 
Dato: AÑO (Variable tipo Entero, almacena el año a evaluar).
Un año bisiesto es aquel múltiplo de 4 pero no de 100 o si es múltiplo de 400.
"""

año = int(input("Ingrese el año: "))

if ((año % 4 == 0)and(año % 100 != 0))or(año % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")