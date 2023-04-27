"""Blogly application."""

import os

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
# TODO: add classes to from models once created
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///blogly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

@app.get("/")
def go_home():
    return redirect('/users')

@app.get('/users')
def show_users():
    #retrieve users and pass users to users.html page to be rendered

    return render_template("users.html")

@app.get('/users/new')
def user_form():
    return render_template("new_user_form.html")

@app.post('/users/new')
def add_user():
    #process the form info adding the new user to DB
    return redirect("/users")

@app.get('/users/<int:user-id>')
def show_info():
    #show info of given user <user-id>
    return render_template("user_details.html")

@app.get('/users/<int:user-id>/edit')
def edit_user():
    return render_template("user_edit.html")

@app.post('/users/<int:user-id>/edit')
def edit_and_redirect():
    return redirect("/users")

@app.post('/users/<int:user-id>/delete')
def delete_and_redirect():
    return redirect("/users")

