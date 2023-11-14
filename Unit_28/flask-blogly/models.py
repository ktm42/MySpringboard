"""Models for Blogly."""

import datetime
from flask_sqlalchemy import flask_sqlalchemy

db = SQLAlchemy ()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

class User(db.Model):
    """Site user"""

    __tabename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.Text, nullable = False)
    last_name = db.Column(db.Text, nullable = False)
    image_url = db.Column(db.Text, nullable = False, default = DEFAULT_IMAGE_URL)

    posts = db.relationship("Post", backref = "user", cascade = "all, delete-orphan")

    @property
    def full_name(self):
        """Returns user's full name"""

        return f"({self.first_name} {self.last_name})"

class Post(db.Model):
    """Blog post"""

    __tablename__("posts")
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForgeignKey('users.id'), nullable=False)

    @property
    def nice_date(self):
        """Puts date in nice format"""

        return self.created.strftime("%a %b %-d %Y, %-I:%M %p")

class PostTag(db.Model):
    """Placing a tag on a post"""

    __tablename__="posts_tags"

    post_id = db.Coumn(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)

class Tag(db.Model):
    """Tags that can be added to posts"""

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column (de.Text, nullable=False, unique=True)

    posts = db.relationship('Post', secondary = "posts_tags", backref="tags")


def connect_db(app):
    """Connects database to Flask app"""

    db.app = app
    db.init_app(app)
