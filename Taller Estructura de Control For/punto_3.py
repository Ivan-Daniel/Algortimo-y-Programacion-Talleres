"""Cuente e Imprima cuantos paises que hay en el archivo"""
archivo=open("paises.txt", "r")
c = 0
lista = []
for i in archivo:
  lista.append(i)
  a =" ".join(lista)
  c+=1
print(len(lista))
archivo.close()