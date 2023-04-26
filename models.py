"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy() #create a SQLAlchemy instance
#create a function that ties your db object to your app object
#thus, allows your flask app to connect to the specified db
def connect_db(app):
   """Connect to database."""
   app.app_context().push()
   db.app = app
   db.init_app(app)