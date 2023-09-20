import os

# print(os.name)

# print(os.environ)

# print(os.getcwd())

# print(os.environ['Part'])

#os.mkdir('hello')
os.rmdir('some')

#os.rename('hello', 'some')



#os.remove('/Users/diasmuratbayev/Library/CloudStorage/OneDrive-Личная/Documents/Курсы/udemy/Python/some/test.txt')


filename = input("Pls enter a name for your file: ")
if os.path.exists(filename):
    print("File exist")
else:
    print("File not exist")