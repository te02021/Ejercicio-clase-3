"""
Dadas las dimensiones de un bloque rectangular, 
calcule las diagonales de las tres caras diferentes. 
Muestre el valor de la mayor diagonal.
"""
largo = float(input("Ingrese el largo del bloque rectangular: "))
alto = float(input("Ingrese el alto del bloque rectangular: "))
ancho = float(input("Ingrese el ancho del bloque rectangular: "))

diagonal1 = (alto**2 + ancho**2)**0.5
diagonal2 = (alto**2 + largo**2)**0.5
diagonal3 = (largo**2 + ancho**2)**0.5

diagonalmayor = diagonal1

if (diagonal2 > diagonal1)and(diagonal2 > diagonal3):
    diagonalmayor = diagonal2
elif (diagonal3 > diagonal1)and(diagonal3 > diagonal2):
    diagonalmayor = diagonal3

print("El valor de la mayor diagonal es: ", diagonalmayor)