from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class New_article(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    content = TextAreaField(label='Content', validators=[DataRequired()])
    submit = SubmitField(label='Post')