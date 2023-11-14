"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisissecret'

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def root():
    """Shows blog posts starting with most recent"""

    posts = Post.query.order_by(Post.created.desc()).limit(7).all()
    return render_template("posts/homepage.html", posts=posts)

@app.errorhandler(404)
def page_not_found():
    """Shows 404 page not found error"""

    return render_template('404.html'), 404

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


@app.route('/users/<int:user_id>/posts/new')
def new_post_form(user_id):
    """New post form for user"""

    user = User.query.get_or_404(user_id)
    return render_template('new-post.html', user=user)

@app.route('/users/int:user_id>/posts/new', methods=['POST'])
def new_posts(user_id):
    """Handles new post form submission"""

    user = User.query.get_or_404(user_id)
    new_post = Post(title=request.form['title'], content=request.form['content'], user=user)

    db.session.add(new_post)
    db.session.commit()
    flash(f"Post '{new_post.title}' was added.")

    return redirect(f'/users/{user_id}')

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    """Page with specific post infromtion"""

    post = Post.query.get_or_404(post_id)
    return render_template('show-post.html', post=post)

@app.route('/posts/int:post_id>/edit')
def edit_post(post_id):
    """Shows form to edit a published post"""

    post = Post.query.get_or_404(post_id)
    return render_template('edit-post.html', post=post)

@app.route('/posts/int:post_id>/edit', methods=['POST'])
def edit_post(post_id):
    """Handles post edit form submission"""

    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']

    db.session.add(post)
    db.session.commit()
    flash(f"Post '{post.title}' edited successfully")

    return redirect(f"/users/{post.user_id}")

@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    """Handle post deletion form submission"""

    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()
    flash(f"Post '{post.title} successfully deleted")

    return redirect(f"/users/{post.user_id}")

@app.route('/tags')
def tags_index():
    """Shows info on all tags"""
    
    tags = Tag.query.all()
    return render_template('tags/index.html', tags=tags)

@app.route('/tags/new')
def new_tag_form():
    """ Form to create a new tag"""
    
    tags = Post.query.all()
    return render_template('new-tags.html', posts=posts)

@app.route('/tags/new', methods=['POST'])
def new_tag():    
    """Handles the form submission for creating a new tag"""

    posts_id = [int(num) for num in request.form.getlist('posts')]
    posts - Post.query.filter(Post.id.in_(post_ids)).all()
    new_tag = tag(name=request.form['name'], posts=posts)

    db.session.add(new_tag)
    db.session.commit()
    flash(f"Tag '{new.tag.name} added.")

    return redirect('/tags')

@app.route('/tags/<int:tag_id>')
def show_tags(tag_id):
    """Shows specific tag info on a page"""

    tag = Tag.query.get_or_404(tag_id)
    return render_template('show-tags.html', tag=tag)

@app.route('/tags/<int:tag_id>/edit')
def edit_tag_form():
    """Form to edit an existing tag"""

    tag = Tag.query.get_or_404(tag_id)
    posts = Post.query.all()
    return render_template('edit-tags.html', tag=tag, posts=posts)

@app.route('/tags/<int:tag_id>/edit', methods=['POST'])
def edit_tags():
    """Handles form submitted to edit a tag"""

    tag = Tag.query.get_or_404(tag_id)
    tag.name = request.form['name']
    post_ids = [int(num) for num in request.form.getlist('posts')]
    tag.posts = Post.query.filter(Post.id.in_(post_ids)).all()

    db.session.add(tag)
    db.session.commit()
    flash(f"Tag '{tag.name}' successfully edited")
    
    return redirect("/tags")

@app.route('/tags/<int:tag_id>/delete', methods=['POST'])
def tags_destroy(tag_id):
    """Handles form submitted to delete a tag"""

    tag = Tag.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()
    flash(f"Tag '{tag.name}' has been deleted.")

    return redirect ('/tags')




