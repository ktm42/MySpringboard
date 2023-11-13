"""Blogly application."""

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
##app.config['SECRET_KEY'] = 'thisissecret'

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def root():
    """Homepage which redirects to user list"""

    return redirect('/users')

@app.route('/users')
def user_info():
    """Shows user information"""
    
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('users/index.html', users = users)

@app.route('/users/new', methods=['GET'])
def new_user_form():
    """Shows the new user form"""

    return render_template('users/new-user.html')

@app.route('/users/new', methods=['POST'])
def new_user():
    """Handle new user form submission"""

    new_user = User(
        first_name = request.form['first_name'],
        last_name = request.form['last_name'],
        image_url = request.form['image_url'] or None
    )

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id')
def show_user(user_id):
    """Shows user-specific info"""

    user = User.query.get_or_404(user_id)
    return render_template('users/show-user.html', user = user)

@app.route('/users/<int:user_id/edit')
def edit_user(user_id):
    """Shows the form to edit user info"""

    user = User.query.get_or_404(user_id)
    return render_template('users/edit-user.html', user = user)

@app.route('/users/<int:user_id>/edit', methods=['POSTS'])
def update_user(user_id):
    """Handle edit user form submission"""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.immage_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    """Handle delet user form submission"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')


