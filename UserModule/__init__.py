from flask import Blueprint,request,render_template,redirect,url_for,session,Response,jsonify
from .forms import LoginForm,RegisterForm
from dbs import C_T_User,C_T_Article
from app import db
UserModule = Blueprint("User_BP",__name__,static_folder="static",template_folder="templates")


@UserModule.route("/login", methods=["POST","GET"])
def login():
    loginform = LoginForm()
    if request.method == "POST":
        if loginform.validate_on_submit():
            username = request.form.get('username')
            password = request.form.get('password')
            red_me = request.form.get('rememberme')
            userobj = C_T_User.query.filter(C_T_User.username==username).first()
            articleobjs = C_T_Article.query.all()
            if userobj != None and userobj.username==username and userobj.password==password:
                session["username"]=username
                session["password"]=password
            return redirect(url_for("index"),code=302)

    return render_template("UserLogin.html", loginform=loginform)


@UserModule.route("/register", methods=["POST","GET"])
def register():
    registerForm = RegisterForm()
    if request.method == "POST":
        if registerForm.validate_on_submit():
            username = request.form.get('username')
            password = request.form.get('password')
            userobj = C_T_User(username=username,password=password)
            db.session.add(userobj)
            db.session.commit()
            return redirect(url_for("User_BP.login"))

    return render_template("UserRegister.html", registerForm=registerForm)


@UserModule.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("index"),code=302)

