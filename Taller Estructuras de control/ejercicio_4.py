"""
Entrada
Costo-->float-->costo
Piezas-->float-->piezas

Salidas
Invertir-->float-->invertir
Prestamo-->float-->prestamo
Credito-->float-->credito
Intereses-->float-->intereses
"""
piezas=float(input("Numero de piezas:"))
costo=float(input("Costo de la pieza:"))
total=piezas*costo
if total>5_000_000:
    invertir=total*.55
    prestamo=total*.30
    credito=total*.15
else:
    invertir=total*.70
    prestamo=0
    credito=total*.30
intereses=credito*.20
print("Cantidad a invertir:",invertir)
print("Cantidad de prestamo:", prestamo)
print("Cantidad de credito:", credito)
print("Intereses: ", intereses)