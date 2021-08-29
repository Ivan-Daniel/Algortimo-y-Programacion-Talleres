p=0
l=0
c=0
while True:
    a=int(input())
    if(a==4):
        break
    else:
        if (a==1):
            p+=1
        elif (a==2):
            l+=1
        elif (a==3):
            c+=1
print("MUITO OBRIGADO")
print("Alcool:",p)
print("Gasolina:",l)
print("Diesel:",c)