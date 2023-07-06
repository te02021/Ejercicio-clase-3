"""
Dados el radio y altura de un cilindro, si la altura es mayor al radio calcule y
muestre el valor del volumen, caso contrario muestre el mensaje: 'Error'
"""

import math

radio = float(input("Ingrese el radio: "))
altura = float(input("Ingrese la altura: "))

if altura > radio:
    volumen = round((math.pi*(radio**2)*altura), 2)
    print("El volumen del cilindro es: ", volumen)
else:
    print("Error")