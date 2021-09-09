"""Busque e imprima el pais de Venezuela y su capital"""
archivo=open("paises.txt", "r")
lista=[]
for i in archivo:
  lista.append(i)
  pc= " ".join(lista)
  if(pc=="Venezuela: Caracas\n"):
    break
  lista=[]
print(pc)
archivo.close()