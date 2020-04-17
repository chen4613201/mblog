from app import db
import time


class C_T_User(db.Model):
    __tablename="m_user"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    email = db.Column(db.String(64))

    def __init__(self,username,password=None,email=None):
        self.username = username
        self.password = password
        self.email = email



class C_T_Article(db.Model):
    __tablename="m_article"
    id = db.Column(db.Integer,primary_key=True)
    artircle_title=db.Column(db.String(128))
    article_content=db.Column(db.Text)
    user_id = db.Column(db.Integer)
    create_time = db.Column(db.TIMESTAMP,default=time.localtime(time.time()))
    read_num = db.Column(db.Integer,default=0)
    #author = db.relationship('C_T_User', backref=db.backref('m_article'))

    def __init__(self,artircle_title,article_content,user_id):
        self.artircle_title = artircle_title
        self.article_content = article_content
        self.user_id = user_id


