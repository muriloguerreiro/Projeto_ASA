from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Required


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")


class AlunoForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    password = StringField('Password: ', validators=[DataRequired()])
    name = StringField('Nome: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired()])

class PerfilForm(FlaskForm):
    user_id = IntegerField('User id: ', validators=[DataRequired()])
    curso = StringField('Curso: ', validators=[DataRequired()])
    periodo = IntegerField('Periodo: ', validators=[DataRequired()])
    disc_1 = StringField('Disciplina 1: ', validators=[DataRequired()])
    nota_d1 = IntegerField('Nota da Disciplina 1: ', validators=[DataRequired()])
    disc_2 = StringField('Disciplina 2: ', validators=[DataRequired()])
    nota_d2 = IntegerField('Nota da Disciplina 1: ', validators=[DataRequired()])
    disc_3 = StringField('Disciplina 3: ', validators=[DataRequired()])
    nota_d3 = IntegerField('Nota da Disciplina 1: ', validators=[DataRequired()])
    disc_4 = StringField('Disciplina 4: ', validators=[DataRequired()])
    nota_d4 = IntegerField('Nota da Disciplina 1: ', validators=[DataRequired()])
