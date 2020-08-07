import sqlite3
import os
os.remove('PLdatabase.db')

connection = sqlite3.connect('PLdatabase.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS friendship(person1 TEXT, person2 TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS houses(name TEXT, person1 Text, person2 TEXT, person3 TEXT, person4 TEXT, covid1 INTEGER, covid2 INTEGER, covid3 INTEGER, covid4 INTEGER )')

friend_const = 100
house_const = 25

def insert_friendship(friend1, friend2):

    with open('relationships.pl', 'a') as f:
        f.write('node({}, {}, {}).\n'.format(
            friend1, friend2, friend_const))


    connection = sqlite3.connect('PLdatabase.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO friendship VALUES ('{friend1}', '{friend2}').".format(
        friend1=friend1, 
        friend2=friend2,
    ))
    connection.commit()
    connection.close()

def insert_house(name, person1, person2, person3, person4, covid1, covid2, covid3, covid4):

    connection = sqlite3.connect('PLdatabase.db')
    cursor = connection.cursor()


    for x in [person1, person2, person3, person4]:
        for y in [person1, person2, person3, person4]:
            if x != y:
                with open('relationships.pl', 'a') as f:
                    f.write('node({}, {}, {})\n'.format(
                        x, y, house_const))

    for c, p in zip([covid1, covid2, covid3, covid4], [person1, person2, person3, person4]):
        if c:
            with open('relationships.pl', 'a') as f:
                f.write('node({}, {}, {})\n'.format(
                    'covid', p, 1))


    cursor.execute("INSERT INTO houses VALUES ('{name}', '{person1}', '{person2}', '{person3}', '{person4}', '{covid1}', '{covid2}', '{covid3}', '{covid4}')".format(
        name=name, 
        person1=person1, 
        person2=person2,
        person3=person3,
        person4=person4,
        covid1 = covid1,
        covid2 = covid2,
        covid3 = covid3,
        covid4 = covid4
    ))
    connection.commit()
    connection.close()


def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    insert_house('test', 't1', 't2', "t3", "t4", 1, 0, 1, 0)
    insert_friendship("test", "friend")


def get_houses():
    connection = sqlite3.connect('PLdatabase.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM houses')
    house_dict = {}
    for row in cursor.fetchall():
        house_dict[row[0]] =[row[1], row[2], row[3], row[4]]

    return house_dict


def get_friendships():
    connection = sqlite3.connect('PLdatabase.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM friendship')
    friendship_list = []
    for row in cursor.fetchall():
        
        friendship_list.append((row[0], row[1]))

    return friendship_list
