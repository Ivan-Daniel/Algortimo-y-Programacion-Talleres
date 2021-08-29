"""
Entradas
valorA-->float-->A
valorB-->float-->B
valorC-->float-->C
Salidas
valor de x1-->str-->x1
valor de x2-->str-->x2
"""
A = float(input("Ingrese el valor de A "))
B = float(input("Ingrese el valor de B "))
C = float(input("Ingrese el valor de C "))
D = B**2-4*A*C
if(D == 0):
  x1 = x2 = -B/(2*A)
  print("El valor de xu es "+str(x1)+" y el valor de x2 es "+str(x2))
elif(D > 0):
  x1 = (-B+(B**2-4*A*C)**0.5)/(2*A)
  x2 = (-B-(B**2-4*A*C)**0.5)/(2*A)
  print("El valor de x1 es "+str(x1)+" y el valor de x2 es "+str(x2))
else:
  print("no tiene solución en los Reales.")