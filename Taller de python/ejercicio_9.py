"""
Entradas
Horas trabajadas-->float-->ht
Pago por hora-->float-->ph
Salidas
Pago junto con la horas-->float-->pa=ht*ph
Descuento por los impuestos-->float-->des1=pa*0.20 y des2=pa-des1
"""
ht=float(input("Digite las horas que ha trabajado: "))
ph=float(input("Digite el pago por hora: "))
pa=ht*ph
des1=pa*0.20 
des2=pa-des1
print("El pago que le daran es de: ", des2)