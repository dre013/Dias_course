import pickle
import os


class Contact:
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return "Name: {0}, \nEmail address: {1}, \nPhone: {2}".format(self.name, self.email, self.phone)

    def change_name(self, name):
        self.name = name
    
    def change_email(self, email):
        self.email = email

    def change_phone(self, phone):
        self.phone = phone
    
def add_contact():
    address_book_file=open('address.txt','rb')
    is_file_empty = os.path.getsize('address.txt') == 0 # True if file is empty
    if not is_file_empty:
        list_contant = pickle.load('address.txt')
    else:
        list_contant = []
    try:
        contact = get_contact_info_from_user()
        address_book_file=open('address.txt','wb')
        list_contant.append(contact)
        pickle.dump(list_contant,address_book_file)
        print("Contact added")
    except KeyboardInterrupt:
        print("Contact not added")
    except EOFError:
        print("Contact not added, problem with file")
    finally:
        address_book_file.close()

def get_contact_info_from_user():
    try:
        contact_name = input("Enter contact name:\n")
        contact_email = input("Enter contact email:\n")
        contact_phone = input("Enter contact phone:\n")
        contact = Contact(contact_name,contact_email,contact_phone)
        return contact
    except EOFError as e :
        raise e #Contact not added
    except KeyboardInterrupt as e:
        raise e

    
def display_contacts():
    address_book_file=open('address.txt','rb')
    is_file_empty = os.path.getsize('address.txt') == 0 # True if file is empty
    if not is_file_empty:
        list_contant = pickle.load(address_book_file)
        for each_contact in list_contant:
            print(each_contact)
    else:
        print("No contact in address")
        return
    address_book_file.close()
    

def search_contant():
    address_book_file=open('address.txt','rb')
    is_file_empty = os.path.getsize('address.txt') == 0 # True if file is empty
    if not is_file_empty:
        search_name = input('Enter the name\n')
        is_contact_found = False
        list_contant = pickle.load(address_book_file)
        for each_contact in list_contant:
            contact_name = each_contact.name
            search_name = search_name.lower() 
            contact_name = contact_name.lower() 
            if(contact_name==search_name):
                print(each_contact)
                is_contact_found = True
                break
        if not is_contact_found: # not False == True
            print("No contact name with the provided search name")
    else:
        print("Address book is empty. No contact to search")
    address_book_file.close()

def delete_contact():
    address_book_file=open('address.txt','rb')
    is_file_empty = os.path.getsize('address.txt') == 0 # True if file is empty
    if not is_file_empty:
        name = input("Enter the name to be deleted\n")
        list_contant = pickle.load(address_book_file)
        is_contact_deleted = False
        for i in range(0,len(list_contant)):
            each_contact = list_contant[i]
            if each_contact.name == name:
                del list_contant[i]
                is_contact_deleted = True
                print("Contact deleted")
                address_book_file=open('address.txt','wb')
                if (len(list_contant)==0):
                    address_book_file.write(b'')
                else:
                    pickle.dump(list_contant,address_book_file)
                break
        if not is_contact_deleted:
            print("No Contact with this name")
    else:
        print("Address book is empty. No contact to delete")
    address_book_file.close()

def modify_contact():
    address_book_file=open('address.txt','rb')
    is_file_empty = os.path.getsize('address.txt') == 0 # True if file is empty
    if not is_file_empty:
        name = input("Enter the name to be modified\n")
        list_contant = pickle.load(address_book_file)
        is_contact_modified = False
        for each_contact in list_contant:
            if each_contact.name == name:
                do_modification(each_contact)
                address_book_file = open('address.txt','wb')
                pickle.dump(list_contant,address_book_file)
                is_contact_modified = True
                print('Contact been modified')
                break
        if not is_contact_modified:
            print("No contact with this name")
    else:
        print("Address book empty.No Contact to modify")

def do_modification(contact):
    try:
        while True:
            print("Enter 1 to modify email\n 2 to modify address \n 3 to modify name \n 4 to quit")
            choise = input()
            if(choise == '1'):
                new_email = input("Please enter a new email: ")
                contact.change_email(new_email)
                break
            elif(choise == '2'):
                new_phone = input("Please enter a new phone number: ")
                contact.change_phone(new_phone)
                break
            elif(choise == '3'):
                new_name = input("Please enter a new name: ")
                contact.change_name(new_name)
                break
            else:
                print("Incorrect  choise")
    except EOFError :
        print("Error by EOFError")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    

print("Enter 'a' to add a contant\n Enter 'b' to browse through contacts\n Enter 'd' to delete contacts\n Enter 'm' to modify contanct \n Enter 's' to search contant \n Enter q to quit ")
while True:
    choise = input("Enter your choise\n")
    if choise.lower() == 'q':
        print("thanks for using our app")
        break
    elif(choise.lower() == 'b'):
        display_contacts()
    elif(choise.lower() == 'a'):
        add_contact()
    elif(choise.lower() == 'd'):
        delete_contact()
    elif(choise.lower() =='m'):
        modify_contact()
    elif(choise.lower() == 's'):
        search_contant()
    else:
        print("Incorrect choise, Need to enter the choise agains")
