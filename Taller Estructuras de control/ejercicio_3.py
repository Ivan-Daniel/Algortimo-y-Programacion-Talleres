"""
Entradas
a-->int-->a
b-->int-->b
c-->int-->c
d-->int-->d
"""
a, b ,c ,d=map(int, input().split())
if d==0:
    x=(a-c)**2
elif d>0:
    x=((a-b)**3)/d
print(x)
