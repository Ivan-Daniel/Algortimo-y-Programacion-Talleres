"""
Entradas
a-->int-->Cantidad prestada
b-->int-->Cantidad pagada
Salidas
d-->int-->Tasa de interes
"""
a=int(input("Prestamo: "))
b=int(input("Valor intereses: "))
inter=(a*4*b)/100
print("La tasa de interes es del ", inter, "%")