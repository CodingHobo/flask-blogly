"""Blogly application."""

import os

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
# TODO: add classes to from models once created
from models import db, connect_db, User, DEFAULT_IMAGE_URL


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
    """redirect to users"""

    return redirect('/users')


@app.get('/users')
def show_users():
    """Retrieve users from DB and pass users to users.html page to be rendered"""

    all_users = User.query.all()
    return render_template("users.html", all_users=all_users)


@app.get('/users/new')
def show_form():
    """render the page with form for new user"""

    return render_template("new_user_form.html")


@app.post('/users/new')
def add_user():
    """process the form info adding the new user to DB, redirect to users"""

    info = request.form
    new_user = User(first_name=info["first_name"],
                    last_name=info["last_name"],
                    image_url=info["image_url"] or None)

    db.session.add(new_user)
    db.session.commit()
    return redirect("/users")


@app.get('/users/<int:user_id>')
def show_info(user_id):
    """show info of given user <user_id> on rendered user_details page"""
    # NOTE THE 404!!!
    user_info = User.query.get_or_404(user_id)
    return render_template("user_details.html", user_info=user_info)


@app.get('/users/<int:user_id>/edit')
def edit_user(user_id):
    """Show the edit page with the info of current user"""

    current_user = User.query.get_or_404(user_id)
    return render_template("user_edit.html", current_user=current_user)


@app.post('/users/<int:user_id>/edit')
def edit_and_redirect(user_id):
    """retrieve form data, update user info in DB, return to users"""

    info = request.form
    current_user = User.query.get_or_404(user_id)

    current_user.first_name = info["first_name"]
    current_user.last_name = info["last_name"]
    current_user.image_url = info.get("image_url", DEFAULT_IMAGE_URL)
    if current_user.image_url == "":
        current_user.image_url = DEFAULT_IMAGE_URL
    # db.session.add(current_user)
    db.session.commit()
    return redirect("/users")


@app.post('/users/<int:user_id>/delete')
def delete_and_redirect(user_id):
    """Delete current user from DB, return back to users"""

    current_user = User.query.get_or_404(user_id)

    db.session.delete(current_user)
    db.session.commit()
    return redirect("/users")
