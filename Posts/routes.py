from flask import Blueprint, render_template, url_for, redirect, flash, request, abort
from flask_login import login_required, current_user
from market import db
from market.models import User_post
from Posts.forms import New_article

posts = Blueprint('posts', __name__)

# ROUTE TO CREATE NEW ARTICLE
@posts.route('/article', methods=['GET', 'POST'])
@login_required
def new_article():
    form = New_article()

    if form.validate_on_submit():
        post = User_post(title = form.title.data, content = form.content.data, author = current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))

    return render_template('create-article.html', title = 'New Article', form=form, legend='New Post')

@posts.route('/update/<int:article_id>', methods=['GET', 'POST'])
@login_required
def update_article(article_id):
    post = User_post.query.get_or_404(article_id)
    if post.author != current_user:
        abort(403)
    form = New_article()
    # UPDATE THE ARTICLE TITLE AND CONTENT
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        return redirect(url_for('users.view_article', article_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content

    return render_template('update.html', title = 'Update', form=form, legend='Edit Article', post=post)

@posts.route('/delete/<int:article_id>', methods=['GET'])
@login_required
def delete_article(article_id):
    post = User_post.query.get_or_404(article_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))