from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Email,Length,EqualTo
from ..models import User
from wtforms import ValidationError