# -*- coding: utf-8 -*-
from app import db
import time


class User(db.model):
    __tablename__="user"
    userid=db.Column(db.INT,primary_key=True,unique=True,autoincrement=1,nullable=False,default=1)
    username=db.Column(db.VARCHAR(50))
    email=db.Column(db.VARCHAR(50))
    createtime=db.Column(db.TIMESTAMP,default=int(time.time()))


class Article(db.model):
    __tablename__="article"
    articleid=db.Column(db.INT(10),primary_key=True,unique=True,autoincrement=1,nullable=False,default=1)
    title=db.Column(db.VARCHAR(100))
    content=db.Column(db.TEXT(10000))
    thumbs=db.Column(db.INT,default=0)
    read=db.Column(db.INT,default=0)
    message=db.Column(db.INT,default=0)

