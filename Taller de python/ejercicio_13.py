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
q,w,e,r,t,j,u,p=inp
q=int(q)
w=int(w)
e=int(e)
r=int(r)
t=int(t)
j=int(j)
u=int(u)
p=int(p)
#caja negra
i=(q*50000)+(w*20000)+(e*10000)+(r*5000)+(t*2000)+(j*1000)+(u*500)+(p*100)
print("La cantidad total de dinero es "+str(i))