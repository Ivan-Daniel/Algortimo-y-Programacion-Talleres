"""Busque e Imprima la ciudad de Singapur"""
archivo = open("paises.txt", "r")
lista_ = []
for i in archivo:
  lista_.append(i)
  a = " ".join(lista_)
  if(a=="Singapur: Singapur\n"):
    break
  lista_=[]
b=a.index(":")
lista=[]
for i in range(0, b):
    lista.append(a[i])
    unir = "".join(lista)
print(unir)
archivo.close()