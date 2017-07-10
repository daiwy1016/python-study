#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask
from flask import request,render_template

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    #return '<h1>HOME</h1>'
    return render_template('home.html')
    
@app.route('/signin',methods=['GET'])
def signin_form():
    #return '''<form action="/signin" method="post">
    #          <p><input name="username"></p>
    #          <p><input name="password" type="password"></p>
    #          <p><button type="submit">Sign In</button></p>
    #          </form>'''
    return render_template('form.html')
@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username']=='admin' and request.form['password']=='admin':
        #return '<h3>hello,%s</h3>'%request.form['username']
        page_list=[1,2,3,4,5]
        return render_template('signin-ok.html', username=request.form['username'],page_list=page_list)
    #return '<h3>bad username or password! %s</h3>'%request.form['username']
    return render_template('form.html', message='Bad username or password', username=request.form['username'])
if __name__=='__main__':
    app.run('',5000)
    #app.run()
    #app.run(host='0.0.0.0',port=8000)
            