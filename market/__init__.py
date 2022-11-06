import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

base_dir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + \
    os.path.join(base_dir, 'blog-app.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'bdbf459ede2cfd0368d3051779272b18f225d8d5'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

def create_flask_app():
    db.init_app(app)
    migrate.init_app(app,db)
    return app

# db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'Users.login'
login_manager.login_message_category = 'info'

from Users.routes import users
from Posts.routes import posts
from main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)