"""
entradas
edad-->int-->edad
hemoglobina-->int-->hemo
salidas
resultado-->str--r
"""
edad = int(input("Su edad en meses "))
hemo = float(input("Su nivel de hemoglobina en % "))
if(edad >= 0 and edad <= 1):
  if(hemo >= 12 and hemo <= 26):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")
elif(edad > 1 and edad <= 6):
  if(hemo >= 10 and hemo <= 18):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")
elif(edad > 6 and edad <= 12):
  if(hemo >= 11 and hemo <= 15):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")
elif(edad > 12 and edad <= 60):
  if(hemo >= 11.5 and hemo <= 15):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")
elif(edad > 60 and edad <= 120):
  if(hemo >= 12.6 and hemo <= 15.5):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")
elif(edad > 120 and edad <= 180):
  if(hemo >= 13 and hemo <= 15.5):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")