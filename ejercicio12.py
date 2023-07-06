"""
Se desea leer por teclado un número comprendido entre 0 y 10 (inclusive) 
y se desea visualizar si el número es par o impar. Validar
"""

numero = int(input("Ingrese el numero: "))

while (numero > 10)or(numero<0):
    numero = int(input("Ingrese el numero: "))
if (numero >= 0)and(numero <= 10):
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")