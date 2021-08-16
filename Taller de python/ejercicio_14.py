"""
Entradas
a-->int-->Consumo de energía en kilowatts
b-->int-->Precio por kilowatt
Salidas
c-->int-->Valor a pagar
"""
a=int(input("Digite el consumo en kilowatts"))
b=int(input("Precio por kilowatt"))

c=a*b
print("  "+str(c))