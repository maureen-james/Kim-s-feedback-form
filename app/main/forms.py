from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo
from ..models import User
# from wtforms import ValidationError


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
   
    submit = SubmitField('Submit')


class FeedbackForm(FlaskForm):
    context = StringField('Type of feedback', validators=[DataRequired(), Length(1, 64)])
    company = StringField('Company/organization in question', validators=[DataRequired(), Length(1, 64)])
    post = TextAreaField('Feedback ', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    content = TextAreaField('Feedback Content', validators=[DataRequired()])
    submit = SubmitField('Submit')
