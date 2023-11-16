from flask_sqlalchemy import flask_sqlalchemy

GENERIC_IMAGE = "https//mylostpetalert.com/wp-content/themes/mlpa-child/images/nophonto.gif"

db = SQLAlchemy()

class Pet(db.Model):
    """Adoptable Pets"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable = False, default = True)

    def image_url(self):
        """Shows image for pet or generic image"""

        return self.photo_url or GENERIC_IMAGE

def connect_db(app):
    """Connect database to Flask app"""

    db.app = app
    db.init_app(app)
    