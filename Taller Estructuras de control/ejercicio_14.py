"""
Entrada
Lectrua anteriror-->float-->la
Lectura actual-->flaot-->lac
Salida
Pago a hacer-->float-->p
"""
la, lac=map(float, input("Digite los Kilovatios/kwh consumidos en el mes pasado y en este:").split())
kv = lac-la
if(kv >= 0 and kv <= 100):
  p = kv*4600
  print("Total a pagar $",p)
elif(kv >= 101 and kv <= 300):
  p = kv*8000
  print("Total a pagar $",p)
elif(kv >= 301 and kv <= 500):
  p = kv*100000
  print("Total a pagar $",p)
else:
  p = kv*120000
  print("Total a pagar $",p)