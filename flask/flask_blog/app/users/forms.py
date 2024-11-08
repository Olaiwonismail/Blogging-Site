from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField,EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                                validators = [DataRequired(),Length(min=2,max =20)])
    email = EmailField('Email',
                                validators = [DataRequired()])
    password = PasswordField('Password' ,validators = [DataRequired()] )
    confirm_password = PasswordField('Confirm Password',validators = [DataRequired(),EqualTo('password')] )

    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This user name has been taken Please choose another')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email has been taken Please choose another')

class LoginForm(FlaskForm):

    email = EmailField('Email',
                                validators = [DataRequired()])
    password = PasswordField('Password' ,validators = [DataRequired()] )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                                validators = [DataRequired(),Length(min=2,max =20)])

    email = EmailField('Email',
                                validators = [DataRequired()])
    picture = FileField('Update Profile Picture',validators = [FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_username(self,username):
        if username.data != current_user.username:

            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This user name has been taken Please choose another')
        else:
            raise ValidationError('you cant use the same')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email has been taken Please choose another')
        else:
            raise ValidationError('you cant use the same')

class RequestResetForm(FlaskForm):
    email = EmailField('Email',
                                validators = [DataRequired()])
    submit = SubmitField('Submit')
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Email doesn exist')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password' ,validators = [DataRequired()] )
    confirm_password = PasswordField('Confirm Password',validators = [DataRequired(),EqualTo('password')] )
    submit = SubmitField('Reset')
