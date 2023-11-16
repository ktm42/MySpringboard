from flask import Flask, url_for, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yetanothersecret'

app.cofig['SQLALCHEMY_DATABASE_URI'] = 'postgresql://adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)

@app.route('/')
def pet_list():
    """List of all the pets"""

    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Add a pet to list for adoption"""

    form = AddPetForm()
    
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != 'csrf_token'}
        new_pet = Pet(name=form.name.data, age=form.age.data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} has been added")
        return redirec(url_for('list_pets'))

    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/int: pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Edit pet info"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} has been updated")
        return redirect(url_for('list_pets'))

    else:
        return render_template('edit_pet_form.html', form=form, pet=pet)

@app.route('/api/pets/<int:ped_id>', methods=['GET'])
def api_get_pet(pet_id):
    """Returns info about pets in JSON"""

    pet = Pet.query.get_or_404(pet_id)
    ingo = {'name': pet.name, 'age': pet.age}

    return jsonify(info)   

