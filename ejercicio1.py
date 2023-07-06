"""
Dados el radio y altura de un cilindro, si la altura es mayor al radio calcule y 
muestre el valor del volumen del cilindro, caso contrario muestre el valor del área del cilindro.
"""
import math


radio = float(input("Ingrese el radio: "))
altura = float(input("Ingrese la altura: "))

if altura > radio:
    volumen = round((math.pi*(radio**2)*altura), 2)
    print("El volumen del cilindro es: ", volumen)
else:
    area = round((2*math.pi*radio*(radio + altura)), 2)
    print("El area del cilindro es: ", area)
    