from app import app
from waitress import serve
from flask import render_template, request
import os

# pip3 install flask
# pip3 install waitress


os.environ['GLOG_minloglevel'] = '2'
@app.route('/submit_house', methods=['POST'])
def proc_house():
    text = request.form['text']
    try:
        chb = request.form['covid']
        chb = True
    except:
        chb = False
    print(text, chb)
    print(render_template('base.html', msg="User has been added to database"))
    return render_template('base.html', msg="User has been added to database")

@app.route('/submit_friends', methods=['POST'])
def proc_friend():
    friend1 = request.form["friend1"]
    friend2 = request.form["friend2"]
    print(friend1, friend2)
    return render_template('base.html', Friends="{} and {} are now friends".format(friend1, friend2))

@app.route('/')
def open_fn():
    return render_template('base.html')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)
