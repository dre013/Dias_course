#Решение к 1 заданию
def average(arr):
    temp = 0
    temp1 = set(arr)
    count = len(temp1)
    for i in temp1:
        temp+=i
    res = temp/count
    return res

arr1 = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
print(average(arr1))

#Решение к 2 заданию
n = int(input('Введите кол-во желаемых объектов: '))
arr = set()
for i in range(n):
    arr.add(input('Введите название объекта: '))
print(len(arr))

#Решение к 3 заданию
a = int(input())
for i in range(a):
    b = set(input().split())
c = int(input())
for i in range(c):
    d = set(input().split())
res = b.symmetric_difference(d)
print(len(res))


#Решение к 4 заданию
a = int(input())
c = int(input())

for i in range(a):
    b = set(input().split())

for i in range(c):
    d = set(input().split())

res = b.difference(d)
print(len(res))

#Решение к 5 заданию
a = int(input())
c = int(input())

for i in range(a):
    b = set(input().split())
    
for i in range(c):
    d = set(input().split())

res = b.intersection(d)
print(len(res))


#Решение к 6 заданию

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
c = int(input())

for i in range(a):
    b = set(input().split())

for i in range(c):
    d = set(input().split())

res = b.union(d)
print(len(res))
