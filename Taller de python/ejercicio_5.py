"""
Entradas
Calificaciones parciales-->float-->cp=(n1,n2,n3)=55%
Examen fianl-->float-->ef=30%
trabajo final-->float-->tf=15%

Salidas
Promedio-->float-->pr=(n1+n2+n3)/3*0.55
Nota final-->float-->nf=pr+ef+tf

"""
print("Digite las notas de los 3 parciales:")
n1, n2, n3 = map(int, input().split())
ef=float(input("Digite la nota del examen final: " ))* 0.30
tf=float(input("Digite la nota del trabajo final: "))* 0.15
#Caja negra
pr=(n1+n2+n3)/3*0.55
nf=pr+ef+tf
print("La nota final de la clase de computo es de: ",nf)
