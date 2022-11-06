from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import login_required, current_user, login_user, logout_user
from market import db, bcrypt
from market.models import User, User_post
from Users.form import Regitration_form, Login_form, Update_form, Contact_form
from Users.utils import save_image

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = Regitration_form()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        username=form.username.data,
                        email=form.email.data,
                        password_hash=hashed_pw
                        )
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully', 'success')
        return redirect(url_for('users.login'))

    return render_template('register.html', title = 'Register', form=form)

# LOGIN ROUTE
@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = Login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            next = request.args.get('next')
            return redirect(next) if next else redirect(url_for('main.home'))
        else:
            flash('Login unsuccessful. Check email and password!', 'danger')

    return render_template('login.html', title = 'Login', form=form)

# LOGOUT ROUTE
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))

#  USER ACCOUNT ROUTE
@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = Update_form()

    if form.validate_on_submit():
        if form.image.data:
            image_file = save_image(form.image.data)
            current_user.image_profile = image_file
# TO UPDATE USER ACCOUNT
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        current_user.username = form.username.data
        db.session.commit()
        flash('Account updated!', 'success')
        return redirect(url_for('users.account'))
# IF REQUEST IS GET, POPULATE THE FIELD WITH THE USER INPUT
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
        form.username.data = current_user.username
        
    image_profile = url_for('static', filename='profile_pics/' + current_user.image_profile)
    return render_template('account.html', title = 'Account', image_profile=image_profile, form=form)

# ROUTE TO GET INVIDUAL ARTICLE
@users.route('/article/<int:article_id>')
def view_article(article_id):
    post = User_post.query.get_or_404(article_id)
    return render_template('get-article.html', title=post.title, post=post)

@users.route('/contact', methods=['GET', 'POST'])
def contact():
    form = Contact_form()
    if form.validate_on_submit():
        return redirect(url_for('main.home'))
    return render_template('contact.html', title='Contact', form=form)
