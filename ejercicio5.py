"""
Lea un número. Determine si es entero y múltiplo de 7.
"""

numero = float(input("Ingrese el numero: "))

if numero % 1 == 0:
    print("El numero es entero")
    if numero % 7 == 0:
        print("Tambien es multiplo de 7")
    else:
        print("Pero, no es multiplo de 7")
else:
    print("El numero no es entero")
    print("Tampoco es multiplo de 7")