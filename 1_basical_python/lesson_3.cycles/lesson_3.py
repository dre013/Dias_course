# temp = [2,3,4,5,6]
# arr = len(temp)
# for i in range(arr):
#     print(temp[i])

# temp = 'Hello World'
# print(len(temp))
# for i in range(len(temp)):
#     print(temp[i])

# temp = [1,2,3,4,5,6,7,8,9,10]

# for i in range(len(temp)):
#     if temp[i] % 2 == 0:
#         #print("This number is",temp[i])
#         print(f'This number is even {temp[i]}')
#     else:
#         #print("This number is odd",temp[i])
#         print(f'This number is odd {temp[i]}')

# Find pairs sum is equal to zero
# list1 = [2,4,-5,6,8,-2]
# list2 = [2,-6,8,3,5,-2]

# pars = []

# for i in list1:
#     for j in list2:
#         res = i+j
#         if res == 0:
#             pars.append((i,j))
# print(pars)

vals = [1,2,3,4,5,6,7,8,9,10]
sum = 0
i = 0
while i < len(vals):
    if vals[i] % 2 == 0:
        continue
    else:
        sum += vals[i]
        print(vals[i])
    if sum > 10:
        break
print(sum)