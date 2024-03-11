##caso 1
p= "hoy es lunes"

long=len(p)-1
for j in range(5):
    print(p[long],j,long)
    long=long-1

 ##caso2   
long=len(p)-1
for j in range(11,-1,-1):
    print(p[j],j)

##caso3
s=''
long=len(p)-1
for j in range(long+1):
    s=s+p[long]
    long=long-1
print(s)
