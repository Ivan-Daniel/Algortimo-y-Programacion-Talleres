"""
Entradas
dia-->int--n>d
mes-->int-->nm
Salidas
singno-->int->s
"""
nd = int(input("Numero de dia: "))
nm = int(input("Numero de mes: "))

if (nd >= 21 and nm == 3) or (nd <= 20 and nm == 4):
    print("Aries")
if (nd >= 24 and nm == 9) or (nd <= 23 and nm == 10):
    print("Libra")
if (nd >= 21 and nm == 4) or (nd <= 21 and nm == 5):
    print("Tauro")
if (nd >= 24 and nm == 10) or (nd <= 22 and nm == 11):
    print("Escorpio")
if (nd >= 22 and nm == 5) or (nd <= 21 and nm == 6):
    print("Geminis")
if (nd >= 23 and nm == 11) or (nd <= 21 and nm == 12):
    print("Sagitario")
if (nd >= 21 and nm == 6) or (nd <= 23 and nm == 7):
    print("Cancer")
if (nd >= 22 and nm == 12) or (nd <= 20 and nm == 1):
    print("Capricornio")
if (nd >= 24 and nm == 7) or (nd <= 23 and nm == 8):
    print("Leo")
if (nd >= 21 and nm == 1) or (nd <= 19 and nm == 2):
    print("Acuario")
if (nd >= 24 and nm == 8) or (nd <= 23 and nm == 9):
    print("Virgo")
if (nd >= 20 and nm == 2) or (nd <= 20 and nm == 3):
    print("Piscis")