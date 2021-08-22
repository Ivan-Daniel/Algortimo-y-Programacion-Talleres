"""
Entradas
a-->int-->a
b-->int-->b
c-->int-->c
d-->int-->d
"""
a, b, c ,d=map(int, input("Digite los 4 valores:").split())
#caja negra
e=str(c)+str(d)
f=int(e)
if (f<=50):
    print(str(a)+str(b)+"00")
else:
    print(str(a)+str(b+1)+"00")