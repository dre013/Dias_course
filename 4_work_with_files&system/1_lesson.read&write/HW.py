# f = open("abc.txt", "r")                      #1
# print(*f)

# f = open("abc.txt", "r")                      #2

# try:
#     print(*f)
# except:
#     pass
# finally:
#     f.close()


# with open("abc.txt") as f:                    #3
    
#     my_line = f.readline()
#     my_line2 = f.readlines()
#     f.close()
#     print(*my_line)
#     print(*my_line2)

# with open("abc.txt") as f:
#     for line in f:
#         print(line)

# f = open("zxc.txt", "w")                        #4
# f.write("Hello world")
# f.close()

# f = open("zxc.txt", "r")
# line = f.readline()
# print(line)
# f.close()

# import os                                         #метод переименования

# os.rename("abs.txt", "abc.txt")

f = open("test.txt", "w")
t = open("abc.txt", "r")

for line in t:
    f.write(line)
    
f.close()
t.close()

f = open("test.txt", "r")

while True:
    lines = f.readline()
    if len(lines) == 0:
        break
    print(lines, end = "")
f.close()