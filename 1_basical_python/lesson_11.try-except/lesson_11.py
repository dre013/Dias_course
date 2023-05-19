# string = "5"
# number = int(string)
# print(number)

# string = "hello"
# number = int(string)
# print(number)


# try:
#     инструкции
# except [Тип_исключения]:
#     инструкции



# try:
#     number = int(input("Введите число: "))
#     print("Введенное число:", number)
# except:
#     print("Преобразование прошло неудачно")
# print("Завершение программы")



# try:
#     number = int(input("Введите число: "))
#     print("Введенное число:", number)
# except ValueError:
#     print("Преобразование прошло неудачно")
# print("Завершение программы")



# try:
#     number1 = int(input("Введите первое число: "))
#     number2 = int(input("Введите второе число: "))
#     print("Результат деления:", number1/number2)
# except ValueError:
#     print("Преобразование прошло неудачно")
# except ZeroDivisionError:
#     print("Попытка деления числа на ноль")
# except Exception:
#     print("Общее исключение")
# print("Завершение программы")

# try:
#     number = int(input("Введите число: "))
#     print("Введенное число:", number)
# except ValueError:
#     print("Не удалось преобразовать число")
# finally:
#     print("Блок try завершил выполнение")
# print("Завершение программы")


# try:
#     number = int(input("Введите число: "))
#     print("Введенное число:", number)
# except ValueError as e:
#     print("Сведения об исключении", e)
# print("Завершение программы")

# try:
#     number1 = int(input("Введите первое число: "))
#     number2 = int(input("Введите второе число: "))
#     if number2 == 0:
#         raise Exception("Второе число не должно быть равно 0")
#     print("Результат деления двух чисел:", number1/number2)
# except ValueError:
#     print("Введены некорректные данные")
# except Exception as e:
#     print(e)
# print("Завершение программы")

# def divide(x, y):
#     try:
#         return x / y 
#     except ZeroDivisionError as ex:
#         print(f'An error occured: {ex}')
#     #except TypeError as tp:
#      #   print(f'An error occured: {tp}')
#     except:
#         print("Unknown error occured !")

# divider = input()
# divide(2, divider)

# def divide(x, y):
#     result =  x / y 
#     print("Result calculated")
#     print(result) 

# divide(2, 2)


# file = None
# try:
#     file = open(r'C:\tmp\helloworld.txt')
#     data = file.read()
# except FileNotFoundError as fer:
#     print(f'Error occuder:{fer.strerror}')
# else:
#     print('Smt else')
# finally:
#     if file:
#         file.close()


# def get_int():
#     while True:
#         try:
#             res = int(input("Enter any number: "))
#             return res
#         except:
#             print("Not a number")
#             continue

# print(get_int())

def square (x):
    if x <= 0:
        raise ValueError(f'Вы ввели некорректный вид данных:{x}')
    print(x*4)

square(-4) 


