"""Cuente e Imprima cuantas ciudades inician con la letra M"""
archivo = open("paises.txt", "r")
lista = []
ciudad = []
for i in archivo:
  a = i.index(":")
  for r in range(a+2, len(i)):
    lista.append(i[r])
  a = "".join(lista)
  ciudad.append(a)
  lista = []
for i in ciudad:
	if(i[0] == "M"):
		print(i)
		lista.append(i)
print(len(lista))
archivo.close()