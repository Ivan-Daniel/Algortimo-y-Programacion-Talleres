"""
Entradas
P-->int-->p
Q-->int-->q
"""
p, q=map(int, input("Digite 2 valores:").split())
if p**3+q**4-2*p**2>680:
    print("Los valores "+ str(p),"y", str(q),"satisfacen la expresion")
else:
    print("Los valores "+ str(p),"y",str(q),"no satisfacen la expresion")