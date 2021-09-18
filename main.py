a=int(input())
j=0
while (j<a):
    b=input().split()
    (Brayan,Brigitte)=b
    Brayan=str(Brayan)
    Brigitte=str(Brigitte)
    e="piedra"
    f="papel"
    g="tijera"
    h="lagarto"
    i="holk"
    j=j+1
    
    if (Brayan==e and Brigitte==f):
        print("Caso #"+str(j)+"¡Siempre hay un próximo semestre!")
    elif (Brayan==e and Brigitte==g):
        print("Caso #"+str(j)+"¡LaVidaEsdura!")
    elif (Brayan==e and Brigitte==h):
        print("Caso #"+str(j)+"¡LaVidaEsdura!")
    elif (Brayan==e and Brigitte==i):
        print("Caso #"+str(j)+"¡Siempre hay un próximo semestre!")
    elif (Brayan==e and Brigitte==e):
        print("Caso #"+str(j)+"¡Otra vez!")
    elif (Brayan==f and Brigitte==e):
        print("Caso #"+str(j)+"¡LaVidaEsdura!")
    elif (Brayan==f and Brigitte==g):
        print("Caso #"+str(j)+"¡Siempre hay un próximo semestre!")
    elif (Brayan==f and Brigitte==h): 
        print("Caso #"+str(j)+"¡Siempre hay un próximo semestre!")
    elif (Brayan==f and Brigitte==i): 
        print("Caso #"+str(j)+"¡LaVidaEsdura!")    
    elif (Brayan==f and Brigitte==f): 
        print("Caso #"+str(j)+"¡Otra vez!") 
    elif (Brayan==g and Brigitte==e):
        print("Caso #"+str(j)+"¡Siempre hay un próximo semestre!")
    elif (Brayan==g and Brigitte==f):
        print("Caso #"+str(j)+"¡LaVidaEsdura!")    
    elif (Brayan==g and Brigitte==h):
        print("Caso #"+str(j)+"¡LaVidaEsdura!")
    elif (Brayan==g and Brigitte==i):
        print("Caso #"+str(j)+"¡Siempre hay un próximo semestre!")
    elif (Brayan==g and Brigitte==g):
        print("Caso #"+str(j)+"¡Otra vez!") 
    elif (Brayan==h and Brigitte==e):
        print("Caso #"+str(j)+"¡Siempre hay un próximo semestre!")  
    elif (Brayan==h and Brigitte==f):
        print("Caso #"+str(j)+"¡LaVidaEsdura!")  
    elif (Brayan==h and Brigitte==g):
        print("Caso #"+str(j)+"¡Siempre hay un próximo semestre!")   
    elif (Brayan==h and Brigitte==i):
        print("Caso #"+str(j)+"¡LaVidaEsdura!")   
    elif (Brayan==h and Brigitte==h):
        print("Caso #"+str(j)+"¡Otra vez!")  
    elif (Brayan==i and Brigitte==e):
        print("Caso #"+str(j)+"¡LaVidaEsdura!") 
    elif (Brayan==i and Brigitte==f):
        print("Caso #"+str(j)+"¡Siempre hay un próximo semestre!")  
    elif (Brayan==i and Brigitte==g):
        print("Caso #"+str(j)+"¡LaVidaEsdura!")  
    elif (Brayan==i and Brigitte==h):
        print("Caso #"+str(j)+"¡Siempre hay un próximo semestre!")  
    elif (Brayan==i and Brigitte==i):
        print("Caso #"+str(j)+"¡Otra vez!")  
    else:
        break