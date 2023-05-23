# class person:
#     name = 'Tom'

#     def display_name(self):
#         print(f'Hey, my name is {self.name}')

# person1 = person()
# person1.display_name()

# person2 = person()
# person2.name = 'Dias'
# person2.display_name()

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def display_info(self):
        print(f'Hey, my name is {self.name} and i am {self.age} years old')

person1 = person('Suizy', 32)
person1.display_info()


