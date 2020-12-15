from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Registrar')
    
class PostForm(FlaskForm):
    title = StringField('Titulo', validators=[DataRequired(), Length(max=128)])
    title_slug = StringField('Titulo Slug', validators=[Length(max=128)])
    content = TextAreaField('Contenido')
    submit = SubmitField('enviar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuerdame')
    submit = SubmitField('Login')