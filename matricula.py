matricula=['01234567L','71476342J','63823376M','98376547F']
datos=['nombre','email','telefono','descuento']
p1=['luis gonzalez','luisgonzalez@mail.com','656343576', 12.5]
p2=['macarena ramirez','macarena@mail.com','692839321', 8.0]
p3=['juan jose martinez','juanjo@mail.com','664888233', 5.2]
p4=['carmen sanchez','carmen@mail.com','667677855',15.7]

z=[p1,p2,p3,p4]
x=[]
for i in range(4):
    valores=dict(zip(datos,z[i]))
    x.append(valores)
    
grandi=dict(zip(matricula,x))
print(grandi)
