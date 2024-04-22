import numpy as np
R=6.371
p1=np.array([19.6820765,-101.1927242])
p2=np.array([20.4271039,-101.7398247])

lat =p2[0]-p1[0]
print(lat)
logi = p2[1]-p1[1]
print(logi)
a=np.square(np.sin/(lat/2))+(np.cos(p1[0]))*(np.cos(p2[0]))*(np.square(np.sin(logi/2)))
print(a)
c= 2*(np.arcsin(a))

d=R*c
print(d)

import numpy as np
R=6.371
p1=np.array([19.6820765,-101.1927242])
p2=np.array([20.4271039,-101.7398247])

lat =p2[0]-p1[0]
print(lat)
logi = p2[1]-p1[1]
print(logi)
a=np.square(np.sin/(lat/2))+(np.cos(p1[0]))*(np.cos(p2[0]))*(np.square(np.sin(logi/2)))
print(a)
c= 2*(np.arcsin(a))

d=R*c
print(d)

