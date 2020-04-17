# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config.from_pyfile("config.py")


bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

from dbs import C_T_User,C_T_Article
#db.drop_all()
#db.create_all()
from UserModule import UserModule
from ArticleModule import ArticleModule
app.register_blueprint(UserModule, url_prefix="/user")
app.register_blueprint(ArticleModule, url_prefix="/article")


@app.route('/')
def index():
    article_all = C_T_Article.query.all()
    return render_template("index1.html",contents=article_all)


if __name__ == '__main__':
    print(app.url_map)
    app.run(host='127.0.0.1',port=5000,debug=True)
