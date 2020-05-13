# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,url_for
from flask_bootstrap import Bootstrap
from dbext import db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
app = Flask(__name__)
app.config.from_pyfile("config.py")


bootstrap = Bootstrap(app)
db.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)

from dbs import C_T_User,C_T_Article
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
    app.run()
