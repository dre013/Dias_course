import numpy as np

#1 задание
matrix = np.zeros(10)
print(matrix)
print('''
------------------------------------------
''')

#1.2 задание
matrix = np.zeros((3, 3))
print(matrix)
print('''
------------------------------------------
''')

#2 задание
vector = np.arange(1, 11)
print(vector)
print('''
------------------------------------------
''')

#3 задание
matrix = np.ones([10, 10])
matrix[1:-1,1:-1] = 0
print(matrix)
print('''
------------------------------------------
''')

#4 задание
vector = np.arange(11)
vector = vector[:: -1]
print(vector)
print('''
------------------------------------------
''')

#5 задание
vector = np.arange(10)
vector *= 2
print(vector)
print('''
------------------------------------------
''')

#бонусное задание
def sigmoid (x):
    s = 1/(np.exp(-x) + 1)
    return s 

x = np.array([1, 2, 3])
print(sigmoid(x))

