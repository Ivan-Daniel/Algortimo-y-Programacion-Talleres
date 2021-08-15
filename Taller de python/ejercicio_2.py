""""
Entradas 
capital-->float-->capital
meses-->int-->meses
Salida 
pago-->float-->x
"""
capital=int(input("Digite el dinero que quiere invertir:"))
meses=int(input("Digite los meses que va a estar afiliado:"))
#Caja negra
x=(capital*0.12)*meses
print("Su pago sera de:" ,x)