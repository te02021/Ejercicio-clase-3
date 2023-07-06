"""
Lea la cantidad de Kw que ha consumido una familia y el precio por Kw. 
Si la cantidad es mayor a 700, incremente el precio en 5% para el exceso de Kw sobre 700. 
Muestre el valor total a pagar.
"""

#ingreso de datos

cantidad = float(input("Ingrese la cantidad de Kw que ha consumido: "))
precio = float(input("Ingrese el precio por Kw: "))

if cantidad > 700:
    exceso_kw = (cantidad - 700)
    precio_exceso = precio*1.05
    total = (precio*cantidad) + (exceso_kw*precio_exceso)
else:
    total = (precio*cantidad)

print(total)