"""
entrada
precio_pc-->int-->pc
precio_cuotas-->int-->cuo
salidas
recargo-->str-->r
"""
p=int(input("precio del producto con pago al contado: "))
c = int(input("precio del producto con pago a cuotas: "))
rn=c-p
bro=(rn/c)*100
print("el recargo es de "+ str (bro),"%")