from flask_wtf import FlaskForm
# Import all the fields neccessary to make a form
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, EqualTo


# Create class Sign Up Form that inherits from FlaskForm
class SignUpForm(FlaskForm):
    # use StringField since string is required
    # InputRequired 
    # Similar to "input type=text"
    # First arugment is the text that displays on the screen
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')
