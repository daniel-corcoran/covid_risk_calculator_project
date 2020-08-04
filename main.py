from app import app
from waitress import serve
from flask import render_template, request
import os





os.environ['GLOG_minloglevel'] = '2'
@app.route('/submit', methods=['POST'])
def proc_pst():
    text = request.form['text']
    try:
        (chb := request.form['covid'])
        chb = True
    except:
        chb = False
    print(text, chb)
    return render_template('base.html', msg="User has been added to database")


@app.route('/')
def open_fn():
    return render_template('base.html')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)
