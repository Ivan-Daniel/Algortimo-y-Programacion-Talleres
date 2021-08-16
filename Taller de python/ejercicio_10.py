"""
Entradas
cantidad chelines austriacos-->float-->ca
cantidad dracmas griegos-->float-->dg
cantidad pesetas--> float-->p
Salidas
pesetasr-->lama= ca* chelin
francosFrances-->lamamade= lamama/ franco
dolares-->lamamadela= p*dolar
liras-->p*v100liras
"""
peseta=1
v100chelines=956.871
chelin=v100chelines/100
v100dracma=88.607
dracma=v100dracma/100
franco=20.110
dolar=122.499
v100liras=9.289
liras=v100liras/100

ca=float(input("Digite una cantidad en chelines austriacos: "))
lama= ca* chelin

dg=float(input("Digite una cantidad en dracmas griegos: "))
lamama= dg* dracma
lamamade= lamama/ franco

p=float(input("Digite una cantidad en pesetas: "))
lamamadela= p*dolar
lamamadelamama= p*v100liras

print("De chelines austriacos a pesetas es: ",lama)
print("De dracmas griegos a francos franceses es: ",lamamade)
print("De pesetas a dólares",lamamade, "liras italianas. es: ",lamamadelamama)