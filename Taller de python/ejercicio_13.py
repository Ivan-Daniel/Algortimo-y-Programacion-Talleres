"""
Entradas
a-->int-->Cantidad de billetes de 50000
b-->int-->Cantidad de billetes de 20000
c-->int-->Cantidad de billetes de 10000
d-->int-->Cantidad de billetes de 5000
e-->int-->Cantidad de billetes de 2000
f-->int-->Cantidad de billetes de 1000
g-->int-->Cantidad de billetes de 500
h-->int-->Cantidad de billetes de 100
Salidas
i-->int-->Cantidad total de dinero
"""
inp=input().split()
a,b,c,d,e,f,g,h=inp
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
f=int(f)
g=int(g)
h=int(h)
#caja negra
i=(a*50000)+(b*20000)+(c*10000)+(d*5000)+(e*2000)+(f*1000)+(g*500)+(h*100)
print("La cantidad total de dinero es "+str(i))