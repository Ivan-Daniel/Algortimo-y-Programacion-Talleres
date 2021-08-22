"""
Entradas
Suledo del trabajador-->float-->suledo
Salidas
Nuevo sueldo-->float-->sueldof
"""
sueldo=float(input("Digite su suledo:"))
if sueldo<900_000:
    sueldof=(.15*sueldo)+sueldo
else:
    sueldof=(.12*sueldo)+sueldo
print("Su sueldo es de:",sueldof)