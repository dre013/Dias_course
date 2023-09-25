import psycopg2 as ps
from psycopg2 import Error
from timeit import default_timer as ti
con = ps.connect(dbname='testDB', user='postgres', password='123')
cur = con.cursor()

# Create a new table


def getCreateTable():
    try:
        cur.execute("DROP TABLE IF EXISTS Diary")
        cur.execute(
            "CREATE TABLE Diary (diary_id serial PRIMARY KEY, p_fullname varchar, gender char, age int, city varchar DEFAULT 'Almaty');")
        con.commit()
        print("Table Diary is created successfully")
    except (Exception, Error):
        print("Exception", Error)
    finally:
        cur.close()
        con.close()
        print("Connection is closed successfully")

# Inserting into table Diary


def getInsertTable():
    name, gender, age, city = input(
        "Please enter your attributes by space: ").split()
    try:
        cur.execute("INSERT INTO  Diary (p_fullname, gender,age,city) VALUES(%s, %s,%s, %s)",
                    (name, gender, age, city))
        con.commit()
    except (Exception, Error):
        print("Cannot insert a data", Error)
    finally:
        cur.close()
        con.close()
        print("Connection is closed successfully")


# Update table Diary
def getUpdateTable():
    select, p_id = input(
        "Please enter your attributes separated by space").split()
    if select == 'p_fullname':
        try:
            name = input("Please enter your new name: ")
            cur.execute(
                "UPDATE Diary set p_fullname = %s where diary_id = %s", (name, p_id))
            con.commit()
            print("Updating in table Diary is completed successfully")
        except (Exception, Error):
            print("Cannot update a Full Name", Error)
        finally:
            cur.close()
            con.close()
            print("Connection is closed successfully")
    elif select == 'age':
        age = input("Please enter your new age: ")
        try:
            cur.execute(
                "UPDATE Diary set age = %s where diary_id = %s", (age, p_id))
            con.commit()
            print("Updating in table Diary is completed successfully")
        except (Exception, Error):
            print("Cannot update a age", Error)
        finally:
            cur.close()
            con.close()
            print("Connection is closed successfully")
    elif select == 'city':
        city = input("Please enter your new city: ")
        try:
            cur.execute(
                "UPDATE Diary set city = %s where diary_id = %s", (city, p_id))
            con.commit()
            print("Updating in table Diary is completed successfully")
        except (Exception, Error):
            print("Cannot update a city", Error)
        finally:
            cur.close()
            con.close()
            print("Connection is closed successfully")
    else:
        print("You got a wrong coloum name")

# Delete a row in the table Diary


def getDeleteRow():
    diary_id = input("Please a enter your id: ")
    cur.execute("DELETE FROM Diary where diary_id = %s", (diary_id))
    con.commit()
    print("Deleting in table Diary is completed successfully")

# Delete a all table Diary


def getDeleteTable():
    choose = input("Do you want to delete table ? y/n")
    if choose.lower() == "yes" or choose.lower() == "y":
        choose2 = ("Are you sure about it ? y/n")
        if choose2.lower() == "yes" or choose2.lower() == "y":
            cur.execute("DELETE FROM Diary")
            con.commit()
            print("Deleting in table Diary is completed successfully")
        elif choose2.lower() == "no" or choose2.lower() == "n":
            print("Okey goodbay")
        else:
            print("Unknown command")
    elif choose.lower() == "no" or choose.lower() == "n":
        print("Okey goodbay")
    else:
        print("Unknown command")


# Select all data from diary
def getSelectedData():
    try:
        start = ti()
        cur.execute("SELECT * from Diary")
        fill = cur.fetchall()
        for i in fill:
            print(i)
        end = ti()
        print("Select completed successfully")
        print(f"Select took {end-start} for execution")
    except (Exception, Error):
        print(Error)
    finally:
        cur.close()
        con.close()
        print("Connection is closed successfully")


print("""
    if you want to CREATE a table choose a button 'C'
    if you want to INSERT to table choose a button 'I'
    if you want to UPDATE a table choose a button 'U'
    if you want to DELETE a table choose a button 'D'
    if you want to DELETE a row in table choose a button 'F'
    if you want to SELECT a table choose a button 'S'
    if you want to FINISH a table choose a button 'Q'
""")

while True:
    choise = input("Enter your choice\n")
    if choise.lower() == 'q':
        print("Thanks for using our application")
        cur.close()
        con.close()
        break
    elif (choise.lower() == 'c'):
        getCreateTable()
    elif (choise.lower() == 'i'):
        getInsertTable()
    elif (choise.lower() == 'u'):
        getUpdateTable()
    elif (choise.lower() == 'f'):
        getDeleteRow()
    elif (choise.lower() == 'd'):
        getDeleteTable()
    elif (choise.lower() == 's'):
        getSelectedData()
