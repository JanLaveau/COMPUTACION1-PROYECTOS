materias=['matematicas','ingles','español','computo']
creditos=[10,8,12,7]

valores=dict(zip(materias,creditos))
print(valores)


frutas=['manzana','pera','guayaba','mango']
precios=[30,10,40,50]

valores=dict(zip(frutas,precios))
print("dime una fruta")
x=input()
print(valores.get(x,'NO HAY YA SE ACABO'))

#if valores.keys().index(x)>=0:
#print(valores[x])
#els:
#print('no hay')
