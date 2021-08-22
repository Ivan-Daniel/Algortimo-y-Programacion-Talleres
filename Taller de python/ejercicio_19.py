"""
Entrada
lote-->int-->x
venta-->int-->k
docenas-->int-->y
Salida
descuento-->int-->d
"""
x = int(input("digite el numero de lotes: "))
k= int(input("valor total de ventas: "))
h= int(input("cantidad de docenas: "))
pp = (k*h)-x
a = 100-((x/pp)*100)
print("La ganancia ", a, "%")