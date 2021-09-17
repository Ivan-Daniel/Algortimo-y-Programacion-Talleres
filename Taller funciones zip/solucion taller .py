import copy
frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)


#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
Salidas

def eliminar_un_caracter_de_toda_la_lista(lista:list,elemento:str)->list:
  auxiliar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxiliar.append(a)
  return auxiliar
"""

#Realizar una funcion que retorne la copia de una funcion que pasa por parametro 
"""
Entradas:
Salidas
"""
"""
def copia_lista(lista):
  return lista.copy
"""
#Realizar una funcion que retorne una lista de numeros enteros

"""
Entradas:
Salidas
  
def numeros_enteros(lista:list):
  auxiliar=[]
  auxiliar2=[]
  for i in lista:
    auxiliar.apepend(float(i))
  for i in auxiliar:
    auxiliar2.append(int(i))
  return auxiliar2
"""
#Realiza una funcion que retorne una lista con los numeros pares
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
"""  
def numeros_pares(lista):
  aux=[]
  for i in lista:
    if(float(i)%2==0):
      aux.append(i)
  

#Realizar una funcion que elimine un elemento de una lista
"""
Entradas
lista-->list-->lista
Salidas
lista-->list-->lista
 
def elimina_elemento_lista(lista,elemento):
  lista.remove(elemento)
  return lista
"""
#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas
lista-list-->lista
letra-->str-->letra
Salidas
lista-list-->lista
"""  
"""
def letra(letra:str,lista:list)->list:
  auxiliar=[]
  for i in lista:
    if i ([0]==letra):
      auxiliar.append(i)
  return(auxiliar)
"""
#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas:
Lista-->list-->lista
Salidas
Contar-->float--len
"""   
def tamano_lista(lista):
  for i in lista:
    print (len(lista))
#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas
Lista-->list-->lista
Salidas
Contar-->float-->len
Tipo-->str-->type
type()
len()
"""  
"""
def informacion_lista(lista):
  for i in lista:
    a=len(lista)
    b=type(lista)
  print(a, b)
"""
#Retornar una lista con los numero negativos  
"""
Entradas
Lista-->list-->lista
Salidas
Lista-->list-->lista
"""  
def numeros_negativos(lista):
  aux=[]
  for i in lista:
    if(float(i)<0):
      aux.append(i)
  return aux    
#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
"""
def posicion_elemento(lista:list,elemento:str):
  for i in lista:
    if(i==elemento):
     p=lista.index(i)
     print (p)

"""
#realizar una funcion que agregue al final de archivo frutas una fruta
"""
def frutas(elemento):
  lista.append(elemento)
  return lista
"""

#Realizar una funcion que cuente el numero de veces que se repite un elemento 
"""
def repetir(lista,elemento):
  aux=[]
  for i in lista:
    aux.append(float(i))
  for i in aux:
    p=aux.count(elemento)
  return p 
"""
""" 
if __name__ == "__main__":
 lista=[1,2,3,4,4]
  copy=copia_lista(lista)
  print(copy)
"""
"""
if __name__ == "__main__":
  lista_frutas_2=eliminar_un_caracter_de_toda_la_lista(lista_frutas,"\n")
  print(lista_frutas_2)
"""
"""
if __name__ == "__main__":
  letra("M",lista_frutas)
  print(letra)
"""
"""
if __name__ == "__main__":
  copia_lista(lista_numeros)
  print(copia_lista)
"""



"""
if __name__ == "__main__":
  bytheway=letra("M",pasdp)
  print(bytheway)
"""
