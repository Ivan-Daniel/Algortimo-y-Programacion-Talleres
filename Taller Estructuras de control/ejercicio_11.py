"""
Entradas
Grados fahrenheit-->float-->a
Salidas
deporte-->float-->d
"""
a=float(input("Ingrese los grados farhenheit: "))
#Caja negra
if (a>85):
    d="Natación"
elif (a>70 and a<=85):
    d="Tennis"
elif (a>32 and a<=70):
    d="Golf"
elif (a>10 and a<=32):
    d="Esquí"
else:
    d="Marcha"
print("El deporte sugerido es: ",d) 