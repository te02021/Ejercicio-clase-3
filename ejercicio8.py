"""
Dadas las tres calificaciones de dos estudiantes. 
La calificación final de cada uno es la suma de sus dos mejores calificaciones. 
Muestre un mensaje que indique cual estudiante (1 o 2) tiene la mayor calificación final.
"""

estudiante1 = input("Ingrese el nombre del primer estudiante: ")
estudiante2 = input("Ingrese el nombre del segundo estudiante: ")

nota1est1 = float(input("Ingrese la primer calificacion del primer estudiante: "))
nota2est1 = float(input("Ingrese la segunda calificacion del primer estudiante: "))
nota3est1 = float(input("Ingrese la tercer calificacion del primer estudiante: "))


nota1est2 = float(input("Ingrese la primer calificacion del segundo estudiante: "))
nota2est2 = float(input("Ingrese la segunda calificacion del segundo estudiante: "))
nota3est2 = float(input("Ingrese la tercer calificacion del segundo estudiante: "))


if (nota1est1 >= nota2est1) and (nota1est1 >= nota3est1):
    if (nota2est1 >= nota3est1):
        calificacion1 = nota1est1 + nota2est1
    else:
        calificacion1 = nota1est1 + nota3est1
elif (nota2est1 >= nota1est1) and (nota2est1 >= nota3est1):
    if (nota1est1 >= nota3est1):
        calificacion1 = nota2est1 + nota1est1
    else:
        calificacion1 = nota2est1 + nota3est1
else:
    if nota1est1 >= nota2est1:
        calificacion1 = nota1est1 + nota3est1
    else:
        calificacion1 = nota2est1 + nota3est1


if (nota1est2 >= nota2est2) and (nota1est2 >= nota3est2):
    if (nota2est2 >= nota3est2):
        calificacion2 = nota1est2 + nota2est2
    else:
        calificacion2 = nota1est2 + nota3est2
elif (nota2est2 >= nota1est2) and (nota2est2 >= nota3est2):
    if (nota1est2 >= nota3est2):
        calificacion2 = nota2est2 + nota1est2
    else:
        calificacion2 = nota2est2 + nota3est2
else:
    if nota1est2 >= nota2est2:
        calificacion2 = nota1est2 + nota3est2
    else:
        calificacion2 = nota2est2 + nota3est2

if calificacion1 > calificacion2:
    print(f"El estudiante {estudiante1} tiene la mejor calificacion y es: {calificacion1}")
else:
    print(f"El estudiante {estudiante2} tiene la mejor calificacion y es: {calificacion2}")