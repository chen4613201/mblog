# coding:utf-8
from flask_wtf import FlaskForm
from flask import request
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,length,EqualTo


class LoginForm(FlaskForm):
    username = StringField(label=u"用户名", validators=[DataRequired(u"用户名必填！"),length(8,16,"长度为8-16位")])
    password = PasswordField(label=u"密码", validators=[DataRequired(u"密码必填！")])
    rememberme = BooleanField(label=u"记住密码")
    submit = SubmitField(label="提交")


class RegisterForm(FlaskForm):
    username = StringField(label=u"用户名", validators=[DataRequired(u"用户名必填！"),length(8,16,"长度为8-16位")])
    password = PasswordField(label=u"密码", validators=[DataRequired(u"密码必填！")])
    password2 = PasswordField(label=u"密码", validators=[DataRequired(u"密码必填！"),EqualTo(fieldname="password",message="两次密码不一致！")])
    submit = SubmitField(label="提交")
