from app import app
from waitress import serve
from flask import render_template, request
import os

os.environ['GLOG_minloglevel'] = '2'

@app.route('/submit_house', methods=['POST'])
def proc_house():
    print(request.form)

    address = request.form['address']
    roommate_1 = request.form['member1']
    roommate_2 = request.form['member2']
    roommate_3 = request.form['member3']
    roommate_4 = request.form['member4']

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
    return render_template('base.html', msg="User has been added to database")

@app.route('/submit_friends', methods=['POST'])
def proc_friend():
    friend1 = request.form["friend1"]
    friend2 = request.form["friend2"]
    print(friend1, friend2)
    return render_template('base.html', msg="{} and {} are now friends".format(friend1, friend2))

@app.route('/')
def open_fn():
    return render_template('base.html')


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)
