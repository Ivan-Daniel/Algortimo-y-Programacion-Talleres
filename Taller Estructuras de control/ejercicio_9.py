"""
Entradas
El valor de la compra-->int-->a
Nombre del cliente-->str-->nombre
Salidas
Valor final de la compra-->int-->b
"""
a=int(input("Digite el valor e la compra: "))
nombre=str(input("Digie su nombre: "))
#caja negra
if (a<50000):
    b="El valor de la compra es ",a
elif (a>50000 and a<100000):
    b="El valor de la compra es ",a-(a*0.05)
elif (a>=100000 and a<700000):
    b="El valor de la compra es ",a-(a*0.11)
elif (a>=700000 and a<1500000):
    b="EL valor de la compra es ",a-(a*0.18)
elif (a>=1500000):
    b="El valor de la compra es ",a-(a*0.25)
print("Señor ",nombre, "el valor final es de: ",b)