from sqlalchemy.orm import *
from sqlalchemy.sql import *
from sqlalchemy import *
import time

engine = create_engine('mysql+mysqlconnector://root:Abc1234%@94.191.110.35:3306/mblog', echo=True)
metadata = MetaData(engine)
Article=Table( 'Article',metadata,
    Column('articleid', Integer,primary_key=True),
    Column('title', VARCHAR(100)),
    Column('content', TEXT(10000)),
    Column('thumbs', Integer,default=0),
    Column('read', Integer,default=0),
    Column('message', Integer,default=0),
    Column('create_time',TIMESTAMP,server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
)
Users=Table( 'Users',metadata,
    Column('userid', Integer,primary_key=True),
    Column('username', VARCHAR(10),nullable=False),
    Column('password', VARCHAR(10),nullable=False),
    Column('email', VARCHAR(30),default=None),
    Column('create_time',TIMESTAMP,server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
)



metadata.create_all(engine)
DB_session = engine.connect()

