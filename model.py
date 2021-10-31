from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

class Users(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key = True)
  username = Column(String)
  password = Column(Integer)

'''class Users(Base):
   __tablename__ = ''
   id = Column(Integer,primary_key = True)
   username = Column(String)
   password = Column(Integer)'''

class Idea(Base):
  __tablename__ = 'idea'
  id = Column(Integer, primary_key = True)
  wyi = Column(String)