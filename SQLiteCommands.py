import sqlite3


def insert_person(name, friend, covid):

    connection = sqlite3.connect('PLdatabase.db')
    cursor = connection.cursor()
    print("INSERT INTO people VALUES ('{name}', '{friend}', '{covid}')".format(
        name=name, 
        friend=friend, 
        covid=covid
    ))
    cursor.execute("INSERT INTO people VALUES ('{name}', '{friend}', '{covid}')".format(
        name=name, 
        friend=friend, 
        covid=covid
    ))
    connection.commit()
    connection.close()

def insert_house(name, person1, person2, person3, person4):

    connection = sqlite3.connect('PLdatabase.db')
    cursor = connection.cursor()
    print("INSERT INTO people VALUES ('{name}', '{person1}', '{person2}', '{person3}', '{person4}')".format(
        name=name, 
        person1=person1, 
        person2=person2,
        person3=person3,
        person4=person4
    ))
    cursor.execute("INSERT INTO people VALUES ('{name}', '{person1}', '{person2}', '{person3}', '{person4}')".format(
        name=name,
        person1=person1, 
        person2=person2,
        person3=person3,
        person4=person4
    ))
    connection.commit()
    connection.close()