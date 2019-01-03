from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from f5InterviewProject.models import Post

class FamilyAdd(FlaskForm):
    firstName = StringField('First Name')
    lastName = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Submit')




