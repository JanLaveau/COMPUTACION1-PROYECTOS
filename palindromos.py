plm="oso"
inv= ''
for j in range(len(plm)-1,-1,-1):
    inv=inv+plm[j]
if plm==inv:
    print("es un palindromo")
else:
    print("no es palindromo")
