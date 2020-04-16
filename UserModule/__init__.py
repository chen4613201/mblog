from flask import Flask
from flask import Blueprint,request,render_template,redirect,url_for,session,Response,jsonify
import json
from .forms import LoginForm,RegisterForm
User_BP = Blueprint("User_BP",__name__,static_folder="static",template_folder="templates")

@User_BP.route("/firstpage")
def firstpage():
    return render_template("firstPage.html")

@User_BP.route("/login", methods=["POST","GET"])
def login():
    loginform = LoginForm()
    if request.method == "POST":
        if loginform.validate_on_submit():
            username = request.form.get('username')
            password = request.form.get('password')
            red_me = request.form.get('rememberme')
            if red_me == 'y':
                session["username"]=username
                session["password"]=password
                return redirect(url_for("index"))
            return redirect(url_for("index"),code=302)

    return render_template("UserLogin.html", loginform=loginform)


@User_BP.route("/register", methods=["POST","GET"])
def register():
    registerForm = RegisterForm()
    if request.method == "POST":
        if registerForm.validate_on_submit():
            return redirect(url_for("login"))

    return render_template("UserRegister.html", registerForm=registerForm)


@User_BP.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("index"),code=302)

