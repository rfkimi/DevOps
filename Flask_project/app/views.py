#!/usr/bin/env python
# encoding: utf-8
from app import app
from flask import render_template, flash, redirect
from .forms import LoginFrom


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Kimi'}  # fake name
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFrom
    return render_template('login.html',
                           title='Sign In',
                           form=form)