"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # create a SQLAlchemy instance
# create a function that ties your db object to your app object
# thus, allows your flask app to connect to the specified db

DEFAULT_IMAGE_URL = "https://pbs.twimg.com/profile_images/971055567035883520/8uCAWl8v_400x400.jpg"


def connect_db(app):
    """Connect to database."""
    app.app_context().push()
    db.app = app
    db.init_app(app)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    first_name = db.Column(
        db.String(50),
        nullable=False
    )

    last_name = db.Column(
        db.String(50),
        nullable=False
    )

    image_url = db.Column(
        db.Text,
        default=DEFAULT_IMAGE_URL
    )
