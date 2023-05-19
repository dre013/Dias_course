import numpy as np

z = np.zeros(10)
print(z)

z = np.ones(10)
print(z)

z = np.full(10,2.5)
print(z)

z = np.array([1,2,3])
print(z)

z = np.arange(10,50)
print(z)

z = np.ones((10,10))
z[1:-1,1:-1]=0
print(z)

z = np.ones(5)
print(z*4)