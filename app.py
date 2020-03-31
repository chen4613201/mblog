from flask import Flask,render_template

app = Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def index():
    return render_template("index.html")


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
