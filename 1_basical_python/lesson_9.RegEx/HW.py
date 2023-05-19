import re

regex = re.compile('\s+')

#1 задание
result = re.split(r'\D', '100,000,000.000')
print(result)

#2 задание. Входные данные: 2 9587456281 1252478965 79963354789
n = '9587456281'
number = re.findall(r'^[7,8,9]', '9587456281')

if 10<=len(n)<=11:
    if number == ['7'] or number == ['8'] or number == ['9']:
        print('Yes')
    else:
        print('No')
else:
    print('No')

