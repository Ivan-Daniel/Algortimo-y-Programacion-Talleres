a=int(input("Dividendo: "))
b=int(input("Divisor: "))
if a>0 and b>0:
  c= 0
  res= a
  while (res >= b):
    res=res-b
    c=c+1
print(c)