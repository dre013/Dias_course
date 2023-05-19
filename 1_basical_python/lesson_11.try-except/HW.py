# 1 задание
import re


def ex_number():
    try:
        number = int(input('Введите номер телефона: '))
        regex = '^[789]'
        pattern = re.compile(regex)
        cnt = len(str(number))
        if (pattern.search(str(number)) is not None) == False:
            raise Exception(f'This is an invalid number: {number}')
        if 9<cnt<12:
            print('Succesful')
        else:
            raise Exception(f'This is an invalid number: {number}')
    except ValueError:
        print('Incorrect number')
    except Exception as e:
        print('Not correct', e)
    finally:
        print('Program ended')


while True:
    ex_number()


# 2 задание

num_list = []
def sum_num():
    try:
        num = int(input('Enter numbers: '))
        num_list.append(num)
        if num == 0:
            raise Exception(f'Sum of all numbers:', sum(num_list))
        # print("Numbers in list",  sum(num_list))

    except ValueError:
        print('Not correct')
    except Exception as e:
        print('Program ended', e)
        
while True:
    sum_num()