from flask import Blueprint, render_template, request, flash
from market.models import User_post

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = User_post.query.order_by(User_post.date_posted.desc()).\
        paginate(page=page, per_page=2)
    # posts = User_post.query.order_by(User_post.id.desc())
    flash("Welcome to NetBlog", "success")
    return render_template('index.html', posts=posts)

# ABOUT ROUTE
@main.route('/about')
def about_page():
    return render_template('about.html', title = 'About')