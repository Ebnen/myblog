
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,length,Email,EqualTo,ValidationError
from data import session
from  rare import User, Post




class registration(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), length(min=3, max=25)] )
    username = StringField('Username', validators=[DataRequired(),length(min=5, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()] )
    confirm = PasswordField('Confirm-Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')
    
    def validate_email(self,email):
        user = session.query(User).filter_by(email=email.data).first()
        if user:
            raise ValidationError("my friend change email abi u don dy mad ni !!")
        
    def validate_username(self, username):
        user = session.query(User).filter_by(username=username.data).first()
        if user:
            raise ValidationError("nigga e be like u go find anoda name !!")
        
    
    

class login(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),length(min=5, max=15)])
    password = PasswordField('Password',validators=[DataRequired()] )
    remember = BooleanField("Remember me")
    submit = SubmitField('Submit')