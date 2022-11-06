from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from market.models import User

# REGISTRATION FORM
class Regitration_form(FlaskForm):
    first_name = StringField(label='First name', validators=[DataRequired(), Length(max=30)])
    last_name = StringField(label='Last name', validators=[DataRequired(), Length(max=30)])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    username = StringField(label='Username', validators=[DataRequired(), Length(min=6, max=30)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(label='Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Create Account')

# VALIDATES IF USER EXIT
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exist')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exist')

# LOGIN FORM
class Login_form(FlaskForm):
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6)])
    remember = BooleanField(label='Remember Me')
    submit = SubmitField(label='Login')

# UPDATE ACCOUNT FORM
class Update_form(FlaskForm):
    first_name = StringField(label='First name', validators=[DataRequired(), Length(max=30)])
    last_name = StringField(label='Last name', validators=[DataRequired(), Length(max=30)])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    username = StringField(label='Username', validators=[DataRequired(), Length(min=6, max=30)])
    image = FileField(label='Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField(label='Update Account')

# VALIDATES IF UPDATED USER EXIST IN THE DATABASE
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already exist')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already exist')

class Contact_form(FlaskForm):
    first_name = StringField(label='First name', validators=[DataRequired(), Length(max=30)])
    last_name = StringField(label='Last name', validators=[DataRequired(), Length(max=30)])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    message = TextAreaField(label='Message', validators=[DataRequired()])
    submit = SubmitField(label='Send')