"""
Entradas
Sueldo-->float-->sueldo
departamento 1-->float-->dep1
departamento 2-->float-->dep2
departamento 3-->float-->dep3
"""
sueldo=float(input("Digite el sueldo: "))
dep1=float(input("Ventas echas por departamento 1: "))
dep2=float(input("Ventas echas por departamento 2: ")) 
dep3=float(input("Ventas echas por departamento 3: ")) 
vt=dep1+dep2+dep3
x=vt*33/100
if dep1>x:
    dep1=sueldo+sueldo*20/100
else:
    dep1=sueldo
if dep2>x:
    dep2=sueldo+sueldo*20/100
else:
    dep2=sueldo
if dep3>x:
    dep3=sueldo+sueldo*20/100
else:
    dep3=sueldo
print("Los vendedores del dep 1 recibiran un pago de:",dep1)
print("Los vendedores del dep 2 recibiran un pago de:", dep2)
print("Los vendedores del dep 3 recibiran un pago de:", dep3)