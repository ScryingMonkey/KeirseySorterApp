
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

from database_setup import db_connect, create_tables, Base, Questions
import settings

# establish connection to database
def db_connect():
	"""
	Performs database connection using database settings from settings.py.
	Returns sqlalchemy engine instance
	"""
	print URL(**settings.DATABASE)
	return create_engine(URL(**settings.DATABASE))

# Takes in a file path to a txt file and returns a list
# of dictionaries of questions gathered from the text file
def CollectQuestions(filePath):
    file = open(filePath, "r")
    questions = []
    n = 0
    for i, line in enumerate(file):
    #    print "line[:3]: %s" % line[:3]
    #    print "line:...%s" % line
        if line[:3] == "[Q]":
            n+=1
            iQ = line.find("[Q]")
            iA = line.find("(a)")
            iB = line.find("(b)")

            #print "q:...", line[iQ+3:iA].strip()
            #print "a:...", line[iA+3:iB].strip()
            #print "b:...", line[iB+3:].strip()
    #        for i, char in enumerate(line):
    #            if char ==
            question = {'number' : n,
                        'question': line[iQ+3:iA].strip(),
                        'answerA': line[iA+3:iB].strip(),
                        'answerB': line[iB+3:].strip()}
            #print question
            questions.append(question)

        else:
			continue
			
    return questions

#    for q in data:
#        print "%s. %s..." %(q['number'], q['question'])
#        print "(a) ", q['answerA']
#        print "(b) ", q['answerB']
#        print ""

    file.close()

def addQuestions(txtFilePath):
	"""
	Save data in the database
	The method is called for every item pipeline component.
	"""
	#Gather questions from txt file
	questionsList = CollectQuestions(txtFilePath)
	print "...questions gathered"

	#Add questions to database		
	try:
		for q in questionsList:
			print "... ...entering for loop"
			question = Questions(number = q['number'],
									  question = q['question'],
									  answerA = q['answerA'],
									  answerB = q['answerB'] )
			print "%s. %s..." %(q['number'], q['question'])
			session.add(question)
		print "... ...exiting for loop"
		session.commit()
	except:
		print "Failed...."
		session.rollback()
		raise	
	finally:
		session.close()
	return
	
#Base = declarative_base()

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance

engine = db_connect()
Base.metadata.bind = engine
create_tables(engine)
# create a configured "Session" class
Session = sessionmaker(bind=engine)
# create a Session
session = Session()
print "...session created"
path = "static\Keirsey_Sorter.txt"
addQuestions(path)