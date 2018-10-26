#!/usr/bin/env python
# encoding: utf-8
"""
@author: binshao
@file: hello_world.py
@time: 2018/10/26 1:44 PM
"""
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('Hello.html', name=name)


@app.route('/user/<int:user_id>')
def get_user(user_id):
    return 'User ID: %d' % user_id


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    title = request.args.get('title', 'Default')
    return render_template('login.html', title=title)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
