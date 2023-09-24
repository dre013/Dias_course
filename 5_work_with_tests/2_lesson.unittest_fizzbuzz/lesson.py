def getReply(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'Fizzbuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    return ''


# for i in range(1,100):
#     fizz = 'Fizz' if  i % 3 == 0 else i
#     buzz = 'Buzz' if  i % 5 == 0 else i
#     print(f'{fizz} {buzz}' or i)
