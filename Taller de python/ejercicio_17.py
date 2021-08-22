"""
Entrada
presupuesto-->int-->p
Salidas
pre_gineco-->str-->pi
pre_trauma-->str-->pr
pre_pedria-->str-->pe
"""
p=int(input("ingrese el presupuesto "))
pi=(p*0.4)
pr=(p*0.3)
pe=(p*0.3)
print("el presupuesto para ginecologia es de $" + pi)
print("el presupuesto para traumatologia es de $" + pr)
print("el presupuesto para pediatria es de $" + pe)