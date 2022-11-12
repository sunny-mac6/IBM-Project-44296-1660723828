#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 19:32:47 2022

@author: karthikeyantamilarasan
"""

from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)
@app.route('/success/<name>')
def success(name):
    return "welcome %s" %name
@app.route('/login',methods=["post","GET"])
def login():
    if request.method=="post":
        user=request.form["nm"]
        return redirect(url_for("success",name = user))

if __name__=='__main__':
    app.run(debug=True)