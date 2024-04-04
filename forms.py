from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class QuestionForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField('Содержание', validators=[DataRequired()])
    submit = SubmitField('Отправить')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Некорректный email')])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите Пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Регистрация')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
