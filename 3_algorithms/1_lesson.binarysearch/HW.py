def BinarySearch(lys, val):                                     # 1 задание
    first = 0
    last = len(lys)-1
    print(last+1)
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index


print(BinarySearch(
["Aston Martin",
"Bentley",
"BMW",
"Bugatti",
"Ferrari",
"Jaguar",
"Koenigsegg",
"Lamborghini",
"Maserati",
"McLaren",
"Mercedes-Benz",
"Porsche"],
'Ferrari'))


def upper_lower(string):                                # 2 задание

    text = ""
    
    for i in string:
        if i.islower():
            text += i.upper()
        else:
            text += i.lower()
    return text
    
s = "I LovE Python"

print(upper_lower(s))



abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def wrap(string, max_width):

    for i in range(0, len(string), max_width):

        result = string[i: i + max_width]

        if len(result) == max_width:
            print(result)
        else:
            return result


print(wrap(abc, 4))
