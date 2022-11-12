#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 13:20:57 2022

@author: karthikeyantamilarasan
"""

from flask import flask,render_template,request,redirect,url_for,session
import ibm_db
import re
app=flask(__name__)
app.secure_key='a'
conn=ibm_db.connect("DATABASE=;HOSTNAME=;PORT=;Security=; SSLServerCertificate=;UID=;PWD=;")
@app.route('/')
def home():
    return render_template('home.html')
@app.route("/login",methods=["get","post"])
def login():
    global userid
    msg="  "
    if request.method=="post" :
        username=request.form['username']
        password=request.form['password']
        sql="select* form user WHERE username=? and password="
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            session["loggedin"]=True
            session['id'] =account["USERNAME"]
            userid=account["USERNAME"]
            session['username']=account["username"]
            msg='logged in sucessfully!'
            return render_template('dashboard.html',msg=msg)
        else:
            msg="incorrect username/password"
    return render_template('login.html', msg=msg)
@app.route('/register',methods=["GET","POST"])
def register():
    msg=" "
    if request.method=="post":
        username=request.form['username']
        email=request.form["email"]
        password=request.form['password']
        sql="select * form user WHERE username=?"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg="account already exist!"
        elif not re.match(r'[^@]+@[^@]+/.[^@]+', email):
            msg="invalid email adress"
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg="name must countain only character and numbers "
        else:
            insert_sql="INSERT INTO user VALUES(?,?,?)"
            prep_stmt=ibm_db.prepare(conn,insert_sql)
            ibm_db.bind_param(prep_stmt,1,username)
            ibm_db.bind_param(prep_stmt,2,email)
            ibm_db.bind_param(prep_stmt,3,password)
            ibm_db.execute(prep_stmt)
            msg='you have logged in sucessfully'
    elif request.method=='POST':
        msg='please fill out of the form'
        return render_template('register.html',msg=msg)
@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')
@app.route('/apply',methods=["GET",'POST'])
def apply():
    msg=" "
    if request.method=="POST":
        username=request.form['username']
        email=request.form['email']
        qualification=request.form['qualification']
        skills=request.form['skills']
        jobs=request.form['s']
        sql="SELECT* FROM users WHERE username=?"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.execute(stmt)
        account=ibm_db.fetc_assoc(stmt)
        
    print(account)
    if account:
        msg="there isonly 1 job posistion!"
        return render_template('apply.html', msg=msg)
    insert_sql="INSERT INTO job VALUES(?,?,?,?,?)"
    prep_stmt=ibm_db.prepare(conn,sql)
    ibm_db.bind_param(prep_stmt,1,username)
    ibm_db.bind_param(prep_stmt,2,email)
    ibm_db.bind_param(prep_stmt,3,skills)
    ibm_db.bind_param(prep_stmt,4,jobs)
    ibm_db.execute(prep_stmt)
    msg="you have loggined sucessfully"
    session['loggedin']=True
   elif request.method=="POST":
        msg='please fill out the form'
        return render_template("app.html",msg=msg)
    @app.route('/display')
    def display():
        print(session["username"],session["id"])
        cursor=mysql.connection.cursor()
        coursor.execute('select* FROM job WHERE userid=%s',session['id'],)
        print("accountdisplay",account)
    
        
    
 
    
      
      
    
    
    
        
            
            
            
            
            
            
        
        

    
        
