# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,url_for
from dbs import *
from sqlalchemy.sql import *
import util

app = Flask(__name__)
app.config['DEBUG']=True


@app.route('/')
def index():
    s = select([Article])
    result=DB_session.execute(s)
    result_list=[]
    for row in result:
        result_tuple={'articleid':row['articleid'],'title':row['title'],'content':row['content']}
        result_list.append(result_tuple)
    return render_template("index.html",contents=result_list)


@app.route('/article/<article_id>')
def article(article_id):
    q = select([Article]).where(Article.c.articleid==article_id)
    result = DB_session.execute(q)
    content={}
    for row in result:
        content = {"id":row['articleid'],"title": row['title'],'content':row['content'],'thumbs':row['thumbs'],'read':row['read'],'message':row['message']}
        print(row)

    return render_template("article.html",contents=content)


@app.route('/edit_article')
def edit_article():
    return render_template("edit_article.html")


@app.route('/submit_article', methods=['POST'])
def submit_article():
    try:
        print(request.form['name'])
        print(request.form['myeditor'])
        Article_Title = request.form['name']
        Article_Content = util.htmlEncodeByRegExp(request.form['myeditor'])
        i=Article.insert().values(title=Article_Title, content=Article_Content)
        DB_session.execute(i)
        return "文章发表成功"
    except Exception as e:
        return "文章发表异常："+str(e)
with app.test_request_context():
    print(url_for('article',article_id=1))

if __name__ == '__main__':
    app.run()
