"""
Entradas
Precio del producto-->int-->pr
Salida
Descuento-->float-->des=pr*0.15
Precio final-->float-->x=pr-des
"""
pr=int(input("Digite el precio del producto: "))
#Caja negra
des=pr*0.15
x=pr-des
print("El precio a pagar es de: ",x)