from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

from database_setup import db_connect, create_tables, Base, Questions
import settings

def QuestionsInDB():
	"""
	Save data in the database
	The method is called for every item pipeline component.
	"""
	#Retrieve first question from database		
	try:
		engine = db_connect()
		Base.metadata.bind = engine
		# create a configured "Session" class
		Session = sessionmaker(bind=engine)
		# create a Session
		session = Session()
		print ".............................................."
		print "...session created.  Querying for questions..."
		questions = session.query(Questions).all()
		print "..........First..."
		question = questions[0]
		print "Printing first question..."
		print question.number, "...", question.question, " : ", question.answerA, " or ", question.answerB
		print "..........Last..."
		question = questions[-1]
		print "Printing first question..."
		print question.number, "...", question.question, " : ", question.answerA, " or ", question.answerB
		print "..........Success............................."
		print ".............................................."

	except:
		print "Failed...."
		raise	
	finally:
		session.close()
	return
	
QuestionsInDB()
