"""imprima la posicion del pais de Uganda"""
archivo=open("paises.txt", "r")
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c+=1
  if(a=="Uganda: Kampala\n"):
    break
  lista = []
print(c)
archivo.close()
