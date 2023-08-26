# # def bubbleSort(x):
# #     n = len(x)

# #     for i in range(n-1):
# #         for j in range(0,n-i-1):
# #             if x[j] > x[j+1]:
# #                 x[j], x[j+1] = x[j+1], x[j]

# # x = [64,68,2,14,675,123,51,2]

# # print(bubbleSort(x))
# # for i in range(len(x)):
# #     print(x[i])

# def selectionSort(x):
#     n = len(x)
#     for i in range(n):
#         min_id = i
#         for j in range(i+1,n):
#             if x[j] < x[min_id]:
#                 min_id = j
#         x[i],x[min_id] = x[min_id], x[i]
#     return x
# x = [64,68,2,14,675,123,51,2]

# print(selectionSort(x))
# for i in range(len(x)):
#     print(x[i])


# # def insersionsort(x):
# #     n = len(x)
# #     for i in range(1,n):
# #         key = x[i]
# #         j = i-1
# #         while x[j] > key and j >=0:
# #             x[j+1] = x[j]
# #             j-=1
# #             x[j+1] = key
# #     return x

# # x = [8,2,3,9,12,57,90]
# # print(insersionsort(x))

# # def quickSort(x):
# #     n = len(x)
# #     if n > 1:
# #         pivot = x.pop()
# #         #grt_lst, eql_lst,sml_lst = [],[pivot],[]
# #         grt_lst = []
# #         eql_lst = [pivot]
# #         sml_lst = []
# #         for i in x:
# #             if i == pivot:
# #                 eql_lst.append(i)
# #             elif i > pivot:
# #                 grt_lst.append(i)
# #             else:
# #                 sml_lst.append(i)
# #         return (quickSort(sml_lst) + eql_lst + quickSort(grt_lst))
# #     else:
# #         return x

# # x = [8,2,3,9,12,57,90]
# # print(quickSort(x))

# def mergeSort(x):
#     n = len(x)
#     if n == 1:
#         return x
#     mid = int(len(x)/2)
#     lst1 = mergeSort(x[:mid])
#     lst2 = mergeSort(x[mid:])
#     result = merge(lst1,lst2)
#     return result

# def merge(lst1,lst2):
#     lst = []
#     i = 0 
#     j = 0 
#     while (i < len(lst1) and j < len(lst2)):
#         if lst1[i] < lst2[j]:
#             lst.append(lst1[i])
#             i+=1
#         else:
#             lst.append(lst2[j])
#             j+=1
#     while (j<=len(lst2)):
#         lst.append(lst2[j])
#         j+=1
#     while (i<=len(lst1)):
#         lst.append(lst1[i])
#         i+=1

#     return lst

# x = [64,68,2,14,675,123,51,2]
# print(mergeSort(x))


import operator

def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


array = [78, 41, 4, 27, 3, 27, 8, 39, 19, 34, 6, 41, 13, 52, 16]
print(merge_sort(array))