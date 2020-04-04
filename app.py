from flask import Flask,render_template

app = Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def index():
    contents = {0:{"title":"nihao","content":"this is 0 neirong",
                   "avatar":"/static/img/logo101_50.png",
                   "username":"chenmingliang",
                   "good":5555,
                   "view":6666,
                   "message":777},
                1:{"title":"今日头条","content":"Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱Windows可谓是大多数人的生产力工具，集娱乐办公于一体，虽然在程序员这个群体中都说苹果是信仰，但是大部分不"},
                2:{"title":"nihao","content":"this is 2 neirong"},
                3:{"title":"nihao","content":"this is 3 neirong"},
                4:{"title":"nihao","content":"this is 4 neirong"},
                5:{"title":"nihao","content":"this is 5 neirong"},}
    return render_template("index.html",contents=contents)


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
