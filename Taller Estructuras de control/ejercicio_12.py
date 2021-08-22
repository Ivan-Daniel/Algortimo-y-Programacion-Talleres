"""
Entradas
valor-->int-->va
"""
a = int(input("Ingrese cantidad de dinero $"))
vcien = (a-a % 100000)/100000
a=a % 100000
vcincuen = (a-a % 50000)/50000
a=a % 50000
vvein = (a-a % 20000)/20000
a=a % 20000
vdiez = (a-a % 10000)/10000
a=a % 10000
vcinco = (a-a % 5000)/5000
a=a % 5000
bd = (a-a % 2000)/2000
a=a % 2000
bm = (a-a % 1000)/1000
a=a % 1000
mq = (a-a % 500)/500
a=a % 500
md = (a-a % 200)/200
a=a % 200
mc = (a-a % 100)/100
a=a % 100
mcq = (a-a % 50)/50
a=a % 50
if vcien>0:
    print("La Cantidad de billetes de 100000 es de: "+str(vcien))
if vcincuen > 0:
    print("La Cantidad de billetes de 50000 es de: "+str(vcincuen))
if vvein > 0:
    print("La Cantidad de billetes de 20000 es de: "+str(vvein))
if vdiez > 0:
    print("La Cantidad de billetes de 10000 es de: "+str(vdiez))
if vcinco > 0:
    print("La Cantidad de billetes de 5000 es de: "+str(vcinco))
if bd > 0:
    print("La Cantidad de billetes de 2000 es de: "+str(bd))
if bm > 0:
    print("La Cantidad de billetes de 1000 es de: "+str(bm))
if mq > 0:
    print("La Cantidad de monedas de 500 es de: "+str(mq))
if md > 0:
    print("La Cantidad de monedas de 200 es de: "+str(md))
if mc > 0:
    print("La Cantidad de monedas de 100 es de: "+str(mc))
if mcq > 0:
    print("La Cantidad de monedas de 50 es de: "+str(mcq))