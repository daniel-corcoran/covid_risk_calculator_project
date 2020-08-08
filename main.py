from app import app
from waitress import serve
from flask import render_template, request
import os
from pyvis.network import Network
import SQLiteCommands

import random
os.remove('relationships.pl')
os.system('touch relationships.pl')
#os.environ['GLOG_minloglevel'] = '2'

# swipl
# consult('shortest_path.pl').
# shortest('X', 'covid', Path, Length).

def gen_iframe():

    friends = SQLiteCommands.get_friendships()
    houses = SQLiteCommands.get_houses()
    net = Network(height="500px", width="100%", bgcolor="#222222", font_color="white", notebook=True, heading='')

    for h in houses:

        import random
        r = lambda: random.randint(150, 255)
        c = '#%02X%02X%02X' % (r(), r(), r())

        for member in houses[h]:
            if member[1] == 'True':
                print(member[0])

                net.add_node(member[0], label=member[0], color='#FF0000')

            else:
                net.add_node(member[0], label=member[0], color=c)
        for member_a in houses[h]:
            for member_b in houses[h]:

                if member_a != member_b:
                    net.add_edge(member_a[0], member_b[0], length=100)

    for f in friends:
        f=list(f)
        net.add_edge(f[0], f[1], length=250)



    net.show('app/static/graph.html')

@app.route('/submit_house', methods=['POST'])
def proc_house():
    print("Hello world")
    print(request.form)

    address = request.form['address']
    roommate_1 = request.form['member1']
    roommate_2 = request.form['member2']
    roommate_3 = request.form['member3']
    roommate_4 = request.form['member4']
    print("Got here")
    try:
        covid_1 = bool(request.form['covid-1'] == 'on')
    except:
        covid_1 = False

    try:
        covid_2 = bool(request.form['covid-2'] == 'on')
    except:
        covid_2 = False

    try:
        covid_3 = bool(request.form['covid-3'] == 'on')
    except:
        covid_3 = False

    try:
        covid_4 = bool(request.form['covid-4'] == 'on')
    except:
        covid_4 = False

    house = {'address': address,
             'roommate 1': {'name': roommate_1, 'covid': covid_1},
             'roommate 2': {'name': roommate_2, 'covid': covid_2},
             'roommate 3': {'name': roommate_3, 'covid': covid_3},
             'roommate 4': {'name': roommate_4, 'covid': covid_4}}


    print("-- house details --")
    for member in house:
        print(member, house[member])
    print("-- end house details --")
    SQLiteCommands.insert_house(address, roommate_1, roommate_2, roommate_3, roommate_4,
                                covid_1, covid_2, covid_3, covid_4)
    gen_iframe()

    return render_template('base.html', iframe_src='/static/graph.html', msg="House has been added to database")

@app.route('/submit_friends', methods=['POST'])
def proc_friend():
    friend1 = request.form["friend1"]
    friend2 = request.form["friend2"]
    print(friend1, friend2)
    SQLiteCommands.insert_friendship(friend1, friend2)
    gen_iframe()
    return render_template('base.html', iframe_src='/static/graph.html', msg="{} and {} are now friends".format(friend1, friend2))

@app.route('/')
def open_fn():
    gen_iframe()
    return render_template('base.html', iframe_src='/static/graph.html')


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)
