import math                                                     
import random 

n = int(input("n: "))                                           # 1 пример. Задача со стековерфлоу
a = float(input("a: "))

items = [random.uniform(-a, a) for i in range(n)]
suma = 0

for i in range(1, n+1):
    j = 0
    z = items[j] if 0 < items[j] < 25 else 2.7
    suma += (z - math.sqrt(z))**2
    j += 1

print(suma)



def rec(a, n):                                                                # 1 задание. Рекуррентные соотношения, быстрое возведение в степень
    return (1 if n == 0
            else rec(a * a, n // 2) if n % 2 == 0
            else a * rec(a, n - 1))

def main():
    x = int(input("a: "))
    y = int(input("b: "))

    print(rec(x, y))

if __name__ == "__main__":
    main()


def collatz(n):                                                                 # 2 задание. Гипотеза Коллатца
    print(n)
    return (n if n == 1
          else collatz(n // 2) if n % 2 == 0
          else collatz(n * 3 + 1))
    
if __name__ == "__main__":
    print(collatz(12))


def binary_search(list, element, start, end):                                      # 3 задание. Рекурсивный бинарный поиск

    mid = 0
    mid = (start + end) // 2

    if list[mid] == element:
        return mid
    elif list[mid] < element:
        return binary_search(list, element, mid + 1, end)
    else:
        return binary_search(list, element, start, mid - 1)


items = [1,2,3,4,5,6,7,8,9,10,11,12]
print(binary_search(items, 8, 0, len(items)))





def check(n, div = None):                                                    # 4 задание. Проверка на простое число
                                                
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            print("Число не является простым")
            return False
        else:
            return check(n, div-1)
    else:
        print("Число является простым")
        return True
    
n = int(input("Введите число: "))
check(n)



def reverse_print(string):                                                     # 5 задание. Рекурсивная обратная печать
    print(string)
    if len(string) == 0:
        return string
    else:
        return reverse_print(string[1:]) + string[0]

string = "hello"
print(reverse_print(string))