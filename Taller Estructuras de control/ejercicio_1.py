"""
Entradas
cantidad invertida-->int-->invertida
Tasa de interes-->float-->tasa
Salida
Saldo-->float-->saldo
"""
invertida=float(input("Cantidad a invertir: "))
tasa=float(input("Tasa de interes: "))

x=invertida*tasa
if x>100_000:
    print("la cantidad generada por concepto de interes es:",x, "supera los 100000")
else:
    print("la cantidad generada por concepto de interes es de:",x, "no supera los 100000")
print("Saldo de la cuenta:",invertida+x )
