my_set= set()
print(my_set)

my_set.add(1)
print(my_set)

my_set.add(2)
print(my_set)


my_set.add(2)
print(my_set)   


print("--------------------------------")
users = {"Tom","Bob","Alice", "Tom"}
print(users)    # {"Tom","Bob","Alice"}


print("--------------------------------")
users = set(["Mike", "Bill", "Ted"])
print(users)    # {"Tom","Bob","Alice"}

#users = set("Mike", "Bill", "Ted")
#   print(users)



users2 = set()
users2 = {"Tom","Bob","Alice"}
print(len(users2) )# 3)



users = set()
users.add("Sam")
print(users)


users = {"Tom", "Bob", "Alice"}
 
user = "Dias"
if user in users: 
    users.remove(user)
print(users)    # {"Bob", "Alice"}

#users.remove("Dias")

user = "Tim"
users.discard(user)
print(users)

users.clear()
print(users)


users = {"Tom","Bob","Alice"}
 
for user in users:
    print(user)

# while user in users:
#     print(user)

users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
 
print(users.issubset(superusers))   # True
print(superusers.issubset(users))   # False

users1 = {"Tom", "Bob", "Alice"}
superusers1 = {"Sam", "Tom", "Bob", "Alice", "Greg"}
print('----------------------------------------------------')
print(users1.issuperset(superusers1)) # False
print(superusers1.issuperset(users1)) # True


users = {"Tom","Bob","Alice"}
users3 = users.copy()
print(users3)

users = {"Tom","Bob","Alice"}
users2 = {"Sam","Kate", "Bob"}
 
users3 = users.union(users2)
print(users3)  
 # {"Bob", "Alice", "Sam", "Kate", "Tom"}
print('----------------------------------------------------')



users = {"Tom","Bob","Alice"}
users2 = {"Sam","Kate", "Bob"}
 
users3 = users.intersection(users2)
print(users3)   # {"Bob"}




users = {"Tom","Bob","Alice"}
users2 = {"Sam","Kate", "Bob"}
 
print(users & users2)   # {"Bob"}


users = {"Tom","Bob","Alice"}
users2 = {"Sam","Kate", "Bob"}
 
users3 = users.difference(users2)
print(users3)           # {"Tom", "Alice"}
print(users - users2)   # {"Tom", "Alice"}


users = frozenset({"Tom", "Bob", "Alice"})


set1 = {'1','2','3'}
set2 = {'4','5','6'}
print(set1.isdisjoint(set2)) #True



set1 = {'1','2','3'}  # 3
set2 = {'1','2','6'}  # 6
set3 = set1.symmetric_difference(set2)
print(set3)

set1 = {'1','2','3'}  # 3
set2 = {'1','2','6'}  # 6
set1.update(set2)
print(set1) # 6 3 2 1


def to_set(element):
    st = set(element)
    return st, len(st)
# Тесты
print(to_set('я обычная строка'))
print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))






#Вторая задача
def diff(set_1, set_2, set_3, symmetric=True):
    if symmetric:
        return set_1 ^ set_2 ^ set_3
    return set_1 - set_2 - set_3

set1 = {'1','2','3'}  # 3
set2 = {'1','2','6'}  # 6
set3 = {'1','2','4'}  # 6

print(diff(set1, set2, set3))

#
print("========================")
def diff(set_1, set_2, set_3, symmetric=True):
    if symmetric:
        return set_1.symmetric_difference(set_2).symmetric_difference(set_3)
    return set_1.difference(set_2, set_3)

# Тесты 
set_1 = {3, 4, 5, 6, 20}
set_2 = {4, 6, 7, 8, 9}
set_3 = {5, 3, 8, 1}

print(diff(set_1, set_2, set_3))
print(diff(set_1, set_2, set_3, symmetric=False))

#третья задача   
def superset(set_1, set_2):
    if set_1 > set_2:
        print(f'Объект {set_1} является чистым супермножеством')
    elif set_1 == set_2:
        print(f'Множества равны')
    elif set_1 < set_2:
        print(f'Объект {set_2} является чистым супермножеством')
    else:
        print('Супермножество не обнаружено')

# Тесты 
set_1 = {1, 8, 3, 5}
set_2 = {3, 5}
set_3 = {5, 3, 8, 1}
set_4 = {90, 100}


superset(set_1, set_2)
superset(set_1, set_3)
superset(set_2, set_3)
superset(set_4, set_2)

#Четвертая задача

def set_gen(lst):

    index = 0
    while index < len(lst):
        cnt = lst.count(lst[index])
        if cnt > 1:
            lst[index] = str(lst[index]) * cnt
        index += 1

    return set(lst)


list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
print(set_gen(list_1))
print(set_gen(list_2))
print(set_gen(list_3))