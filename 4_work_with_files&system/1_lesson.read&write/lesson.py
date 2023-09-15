# f  = open('test.txt','r')
# print(*f)
# print(f)

#метод
# f = open('test.txt','r')
# #действие
# f.close()
# #2 метод
# f = open('test.txt','r')
# #работа что-то делается 
# try:
#     pass
# #действие
# except:
#     pass
# #действие
# finally:
#     f.close()
# #3 метод
# with open('test.txt') as f:
#     pass
#действие

# f = open('test.txt','r')
# print(f.read(10))

# f = open('test.txt','r')
# f.readlines(1)
# print(f.readlines(3))

# f = open('xyz.txt','w')
# f.write('Hello World')
# f.close()

# import os 

# os.rename('test.txt','abc.txt')

poem  = """
    Программирвать весело.
    Если работа скучна
    Чтобы придать ей веселый тон-
    Используй Python!
    """

f = open("poem.txt",'w')
f.write(poem)
f.close()
f=open('poem.txt')

while True:
    line = f.readline()
    if len(line) == 0: 
        break
    print(line, end = '')
f.close()