# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,url_for
from dbs import *
from sqlalchemy.sql import *
import util

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
        #result_tuple={'articleid':row['articleid'],'title':row['title'],'content':row['content']}
        new_article_result_list.append(row)

    for row in hot_article_result:
        print(row)
        #result_tuple={'articleid':row['articleid'],'title':row['title'],'content':row['content']}
        hot_article_result_list.append(row)

    result_set.append(new_article_result_list)
    result_set.append(hot_article_result_list)
    return render_template("index.html",contents=result_set)

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/article/<article_id>')
def article(article_id):
    q = select([Article]).where(Article.c.articleid==article_id)
    result = DB_session.execute(q)
    contents=[]
    for row in result:
        contents.append(row)
        print(row)
    return render_template("article.html",contents=contents)


@app.route('/edit_article')
def edit_article():
    return render_template("edit_article.html")


@app.route('/submit_article', methods=['POST'])
def submit_article():
    try:
        #print(request.form['name'])
        #print(request.form['myeditor'])
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
