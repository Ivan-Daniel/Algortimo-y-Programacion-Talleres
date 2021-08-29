"""
Entradas
Salario del trabajador-->float-->salaraio
Salida
Aumento-->float-->aumento
"""
salario=float(input("Digite su salaraio: "))
if salario>=5_000_000:
    aumento=(salario*.10)+salario
elif salario>=4_300_000:
    aumento=(salario*.15)+salario
elif salario>=3_600_000:
    aumento=(salario*.20)+salario
elif salario>=2_000_000:
    aumento=(salario*.40)+salario
elif salario>=900_000:
    aumento=(salario*.60)+salario
elif salario<=900_000:
    aumento=(salario*60)+salario
print("Su salaraio con su aumento es de: ",str(aumento))

