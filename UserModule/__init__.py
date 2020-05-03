from flask import Blueprint,request,render_template,redirect,url_for,session,Response,jsonify,flash
from .forms import LoginForm,RegisterForm
from dbext import db
from dbs import C_T_User,C_T_Article

UserModule = Blueprint("User_BP",__name__,static_folder="static",template_folder="templates")

from .views import login,register,logout
