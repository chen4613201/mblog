from flask import Flask,render_template

app = Flask(__name__)
app.config['DEBUG']=True

contents = {'0': {"title": "今日重点", "content": "this is 0 neirong",
                "avatar": "/static/img/logo101_50.png",
                "username": "chenmingliang",
                "good": 5555,
                "view": 6666,
                "message": 777},
            '1': {"title": "今日头条", "content": "玖芯科技：p 标签是默认是自动换行的，因此设置好宽度之后，能够较好的实现效果，但是最近的项目中发现，使用 ajax 加载数据之后，p 标签内的内容没有换行，导致布局错乱，于是尝试着使用换行样式，虽然解决了问题，但是并没有发现本质原因，本质在于，我当时获取的数据是一长串的数字，浏览器应该是对数字和英文单词处理方式相近，不会截断。 "},
            '2': {"title": "nihao", "content": "this is 2 neirong"},
            '3': {"title": "nihao", "content": "this is 3 neirong"},
            '4': {"title": "nihao", "content": "this is 4 neirong"},
            '5': {"title": "nihao", "content": "this is 5 neirong"}, }

@app.route('/')
def index():
    return render_template("index.html",contents=contents)

@app.route('/article/<article_id>')
def article(article_id):
    print("adasd:"+article_id)
    print(contents[article_id])
    return render_template("article.html",contents=contents[article_id])

@app.route('/Sentiment')
def Sentiment():
    return render_template("Sentiment.html")


@app.route('/Summary')
def Summary():
    return render_template("Summary.html")

@app.route('/AboutUs')
def AboutUs():
    return render_template("AboutUs.html")


@app.route('/message')
def message():
    return render_template("message.html")

if __name__ == '__main__':
    app.run()
