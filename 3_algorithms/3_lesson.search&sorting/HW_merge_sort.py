def merge_two_list(a, b):    # Объединяет каждые 2 списка
    
    c = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    
    return c

                            
def merge_sort(list):           # Сортирует список

    if len(list) == 1:
        return list
    
    mid = len(list) // 2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge_two_list(left, right)

x = [2,343,3,5,1,6,4,3,76,564,23,41,675,76,23,25]

print(merge_sort(x))