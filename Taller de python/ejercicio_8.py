"""
Entradas
Longitudes de los lados-->float-->a,b,c
Salida
sempiperimetro-->float-->s=(a+b+c)/2
Area-->float-->a=math.sqrt(s*(s-a)*(s-b)*(s-c))
"""
import math
print("Digite las longitudes de los lados del triangulo")
a, b, c = map(int, input().split())
s=(a+b+c)/2
are=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("El area del triangulo es de:",are)