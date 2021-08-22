distancia=float(input("Distancia recorrida en km: "))
if distancia<300:
    pago=50_000
elif distancia>300:
    if distancia<1000:
        pago=70_000+(distancia-300)*30_000
    else:
        pago=150_000+(distancia-300)*9_000
print(pago)
