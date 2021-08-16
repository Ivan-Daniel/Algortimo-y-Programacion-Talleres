"""
Entradas
Nombre del trabajador-->str-->nombre ok
Hijos-->int-->hijos ok
Horas trabajadas-->float-->h ok
Valor de cada hora-->float-->p ok
Horas extras-->float-->he ok
Salidas
Asiganaciones-->float-->asig=as1+as2+as3 ok
Impuestos-->float-->imp=quita1+quita2+quita3 ok
Pago dirigido al trabajador-->float-->pagof=sueldo-imp ok
"""
#Entradas
nombre=str(input("Digite su nombre: "))
hijos=int(input("Digite la cantidad de hijos que ud tenga: "))
h=float(input("Digite las horas trabajadas: "))
p=float(input("Digite el valor asiganado por hora trabajada: "))
he=float(input("Digite las horas extras trabajas: "))
#Caja Negra
ph=p*h# horas*valor
as1=250000#academia
as2=180000#prima
as3=173000*hijos#hijos
p2=(p*0.25)+p#horas extras
phe=p2*he
asig=as1+as2+as3
sueldo=asig+ph+phe
quita1=(sueldo*0.05)#
quita2=(sueldo*0.02)
quita3=(sueldo*0.07)
imp=quita1+quita2+quita3
pagof=sueldo-imp
#Salidas
print("Señor",nombre, "el total de las asignaciones dadas fueron de:",asig, ",las deducciones son de:",imp, "y el sueldo neto del trabajador es de:",pagof)



