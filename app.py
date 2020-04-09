# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,url_for
from dbs import *
from sqlalchemy.sql import *
from forms import *

app = Flask(__name__)
app.config['DEBUG']=True


@app.route('/')
def index():
    new_article = select([Article]).order_by(Article.c.create_time.desc()).limit(10)
    hot_article = select([Article]).order_by(Article.c.read.desc()).limit(10)
    new_article_result=DB_session.execute(new_article)
    hot_article_result=DB_session.execute(hot_article)
    result_set = []
    new_article_result_list = []
    hot_article_result_list = []
    for row in new_article_result:
        new_article_result_list.append(row)
    for row in hot_article_result:
        hot_article_result_list.append(row)
    result_set.append(new_article_result_list)
    result_set.append(hot_article_result_list)
    return render_template("index.html",contents=result_set)


@app.route('/login',methods=["GET","POST"])
def login():
    if request.method =="GET":
        form = LoginForm()
        return render_template("login&register.html",form=form)
    else:
        form = LoginForm(formdata=request.form)
        if form.validate():
            print("用户提交的数据用过格式验证，值为：%s"%form.data)
            return "登录成功"
        else:
            print(form.errors,"错误信息")
        return render_template("login&register.html",form=form)


@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")


@app.route('/article/<article_id>')
def article(article_id):
    q = select([Article]).where(Article.c.articleid==article_id)
    #i = Article.insert()
    result = DB_session.execute(q)
    contents=[]
    for row in result:
        contents.append(row)
    return render_template("article.html",contents=contents)


@app.route('/edit_article')
def edit_article():
    return render_template("edit_article.html")


@app.route('/delete_article/<article_id>')
def delete_article(article_id):
    try:
        #q = select([Article]).where(Article.c.articleid==article_id)
        del_sta = Article.delete().where(Article.c.articleid==article_id)
        #del_sta = delete([Article]).where(Article.c.articleid==article_id)
        print(del_sta)
        #i=Article.insert().values(title=Article_Title, content=Article_Content)
        DB_session.execute(del_sta)
        return "文章删除成功"
    except Exception as e:
        return "文章删除异常："+str(e)
with app.test_request_context():
    print(url_for('article',article_id=1))


@app.route('/submit_article', methods=['POST'])
def submit_article():
    try:
        Article_Title = request.form['name']
        Article_Content = request.form['myeditor']
        i=Article.insert().values(title=Article_Title, content=Article_Content)
        DB_session.execute(i)
        return "文章发表成功"
    except Exception as e:
        return "文章发表异常："+str(e)
with app.test_request_context():
    print(url_for('article',article_id=1))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
