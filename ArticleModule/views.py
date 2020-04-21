from . import ArticleModule
from flask import render_template,request,session,url_for,redirect
from dbs import C_T_Article,C_T_User
from app import db


@ArticleModule.route("/read_article/<articleid>")
def read_article(articleid):
    A_O = C_T_Article.query.filter(C_T_Article.id==articleid).first()
    A_O.read_num = A_O.read_num + 1
    db.session.commit()
    return render_template("article.html",contents=A_O)


@ArticleModule.route("/edit_article",methods=["POST","GET"])
def edit_article():
    print(session.get("username"))
    if request.method=="POST":
        Ar_title = request.form.get("article_title")
        Ar_content = request.form.get("article_content")
        U_obj = C_T_User.query.filter(C_T_User.username==session.get("username")).first()
        A_obj = C_T_Article(artircle_title=Ar_title,article_content=Ar_content,user_id=U_obj.id)
        db.session.add(A_obj)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("edit_article.html")


@ArticleModule.route("/thumbs_up",methods=["GET"])
def thumbs_up():
    articleid = request.args.get("articleid")
    print(articleid)
    a_obj= C_T_Article.query.filter(C_T_Article.id==articleid).first()
    a_obj.thumd_up = a_obj.thumd_up + 1
    db.session.commit()
    return "0"


