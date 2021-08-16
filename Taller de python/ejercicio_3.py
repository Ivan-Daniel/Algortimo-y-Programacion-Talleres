"""
Entradas
Venta uno-->int-->v1
Venta dos-->int-->v2
Venta tres-->int-->v3
Sueldo base-->su-->su
Salidas
Comisiones-->float-->co=((v1+v2+v3)*0.10)
Pago-->float-->x=(su+co)
"""
print("Digite las ventas echas: ")
v1, v2, v3 =map(int, input().split())
su=float(input("Digite su sueldo base: "))
#Caja negra
co=float((v1+v2+v3)*0.10)
x=float(su+co)
print("Su pago es de: ",x)