"""
Entradas
a-->int-->Valor de venta al publico
b-->int-->Valor final 
Salidas
d-->int-->Descuento final
"""
v1=int(input("Valor de venta al publico: "))
v2=int(input("Valor final: "))
a=v2/v1
b=(1-a)*100
print("El descuento aplicado es de "+str("{:.2f}".format(b)+"%"))