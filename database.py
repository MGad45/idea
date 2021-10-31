from model import Base, Users,Idea
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///person.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(username,password):
	user_object=Users(
		username=username,
		password=password
	)
	session.add(user_object)
	session.commit()

def add_idea(wyi):
  idea_object = Idea(wyi = wyi)
  session.add(idea_object)
  session.commit()

def search_user(username):
    user = session.query(Users).filter_by(username = username).first()
    return user

def search_idea(username):
    idea = session.query(Idea).filter_by(username = username).all()
    return idea