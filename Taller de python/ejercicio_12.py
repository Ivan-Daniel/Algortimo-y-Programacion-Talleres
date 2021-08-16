"""
Entradas
examen matematicas-->float-->em
calificacion 3 trabajos-->float-->c1, c2, c3
calificacion fisica--> float-->cf
Salidas
promedio matematicas-->rpromedio1= (em* 0.90)+(tarea* 0.10)
promedio fisica-->promedio2= (cf*0.80)+(tarea1*0.20)
promedio quimica-->promedio3= (cq*0.85)+(tarea2*0.15)
promedio general-->promedio_general = (promedio1 + promedio2 + promedio3) / 3
"""

em=float(input("Escribe la calificacion del examen de matematicas: "))

print("Escribe las calificaciones de los 3 trabajos: ")
c1, c2, c3 =map(float, input().split())
tarea= (c1+c2+c3)/3
promedio1= (em* 0.90)+(tarea* 0.10)

cf=float(input("Escribe la calificacion de la materia de fisica: "))

print("Escribe las calificaciones de los 2 trabajos: ")
v1, v2 =map(float, input().split())
tarea1= (v1+v2)/2
promedio2= (cf*0.80)+(tarea1*0.20)

cq=float(input("Escribe la calificacion de la materia de quimica: " ))

print("Escribe las calificaciones de los 3 trabajos: ")
f1, f2, f3 =map(float, input().split())
tarea2= (f1+f2+f3)/3
promedio3= (cq*0.85)+(tarea2*0.15)

promedio_general = (promedio1 + promedio2 + promedio3) / 3

print("El promedio de matematicas es: ",promedio1)
print("El promedio de fisica es: ", promedio2)
print("El promedio de quimica es: ",promedio3)
print("El promedio general es: ",promedio_general)