from datetime import datetime
from market import db, login_manager
from flask_login import UserMixin

# MANAGES THE USER SESSION
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# USER DATABASE
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    username = db.Column(db.String(30), nullable = False, unique = True)
    email = db.Column(db.String(120), nullable = False, unique = True)
    password_hash = db.Column(db.Text, nullable = False)
    image_profile = db.Column(db.String(20), nullable = False, default='default.jpg')
    posts = db.relationship('User_post', backref='author', lazy=True)

    def __repr__(self):
        return f"User({self.email}, {self.image_profile})"

# USER TITLE AND CONTENT DATABASE
class User_post(db.Model):
    __tablename__ = 'user_post'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"User_post({self.title}, {self.date_posted})"