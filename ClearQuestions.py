from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

import database_setup
import settings

# establish connection to database
def db_connect():
	"""
	Performs database connection using database settings from settings.py.
	Returns sqlalchemy engine instance
	"""
	print URL(**settings.DATABASE)
	return create_engine(URL(**settings.DATABASE))
 
 
#Drop Questions table
def clearQuestions(session):
	print questions
	try:
		Questions.drop(engine, checkfirst=False)
		session.commit()
	except:
		print "Failed...."
		#session.rollback()
		raise	
	return item

Base = declarative_base()
engine = db_connect()
Base.metadata.bind = engine
session = sessionmaker(bind=engine)

clearQuestions(session)