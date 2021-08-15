"""
Entradas
Numero de niños-->int-->nh
Numero de niñas-->int-->nm
Salidas
Porcentaje de niños-->int-->ph
Porcentaje de niñas-->int-->pm
Total de nin@s-->int-->ta
"""
print("Digite el numero de niños y de niñas")
nh, nm = map(int,input().split())
ta= nh+nm
ph=nh*100/ta
pm=nm*100/ta
print("El numero total de miñ@s es: ", ta)
print("El porcentaje de hommbres es: ",ph,"%", "Y el de niñas es de: ", pm,"%")