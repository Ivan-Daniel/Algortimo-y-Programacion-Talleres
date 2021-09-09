"""Imprima la posicion del Pais de Mexico"""
archivo=open("paises.txt", "r")
lista=[]
paises=[]
for i in archivo:
  xd=i.index(":")
  for r in range(0, xd):
    lista.append(i[r])
  xd="".join(lista)
  paises.append(xd)
  lista = []
c=paises.index("México")+1
print(c)
archivo.close()