from flask_sqlalchemy import SQLAlchemy 
from flask_bycrypt import flask_bycrypt

bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    """Connecting database to Flask app"""

    db.app = appdb.init_app(app)
    db.init_app(app)

class User(db.Model):
    """Site user"""

    __tablename__ = 'users'

    username = db.Column(
        db.String(20),
        nullable=Flase,
        unique=True,
        primary_key=True,
    )

    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

    feedback = db.relationship('Feedback', backref='user', cascade='all,delete')

    @classmethod
    def register(cls, username, password, first_name, last_name, email):
        """Register a user and hash the password"""

        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode('utf8')
        user = cls(
            username=username,
            password=hashed_utf8,
            first_name=first_name,
            email=email
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Validate the user exists and used the correct password; if valid, return valid; else False"""

        user = User.query.filter_bay(username=username).first()

        if user and bcrypt.check_password_has(user.password, password):
            return user
        else:
            return False

class Feedback(db.Model):
    """Feedback"""

    __tablename__ = 'feedback'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=Flase)
    username = db.Column(
        db.String(20),
        db.ForeignKey('users.username'),
        nullable=False,
    )
