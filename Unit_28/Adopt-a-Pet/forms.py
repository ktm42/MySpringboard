from flask_wtf import FlaskForm
from wrforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wrforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField('Pet Name', validators = [InputRequired()],)
    species = SelectField('Species', choices = [('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')],)
    photo_url = StringField('Photo URL', validators[Optional(), URL()],)
    age = IntegerField('Age', validators[Optional(), NumberRange(min=0, max =30)],)
    notes = TextAreaField('Comments', validators=[Optional(), Length(min=10)],)
    available = BooleanField('Available?')