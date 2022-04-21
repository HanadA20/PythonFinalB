#2. Using sqlite3, Create a database named pets.
#Create a table (your choice of the name) having
#columns of name, gender, and age with the correct data type for each.
#Enter 5 different pets with data that is inserted in the table.

#Make a query that shows all the female pets. A result from your table must be shown in the Shell.


import sqlite3

connection = sqlite3.connect('Pets')

cursor = connection.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS Pets (name TEXT, gender TEXT, age REAL)')


def data_entry():
    cursor.execute('INSERT INTO Pets VALUES("pipper", "female", 7)')
    cursor.execute('INSERT INTO Pets VALUES("chica", "female", 4)')
    cursor.execute('INSERT INTO Pets VALUES("kenpachi", "male", 12)')
    cursor.execute('INSERT INTO Pets VALUES("blossom", "female", 3)')
    cursor.execute('INSERT INTO Pets VALUES("bamboo", "male", 1)')


def read_from_database():
    cursor.execute('SELECT * FROM Pets WHERE gender = "female"')
    
    data = cursor.fetchall()
    print("1. ", end = "")
    print(data)



connection.commit()

create_table()
data_entry()
read_from_database()
