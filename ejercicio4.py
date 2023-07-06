"""
Lea un número de dos cifras. Determinar si la suma de ambas cifras es un número par o impar. Muestre un mensaje
"""

numero = int(input("Ingrese el numero de dos cifras: "))

unidades = numero % 10

decenas = numero // 10


suma = unidades + decenas

if suma % 2 == 0:
    print(f"La suma de {decenas} y {unidades} es igual a {suma} y es par")
else:
    print(f"La suma de {decenas} y {unidades}  es igual a {suma} y es impar")
    
