from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.engine.url import URL

import settings
 
Base = declarative_base()

# establish connection to database
def db_connect():
	"""
	Performs database connection using database settings from settings.py.
	Returns sqlalchemy engine instance
	"""
	print ".............................................."
	print "...Connecting to Database at URL : "
	print "...attempting URL(**settings.DATABASE)"
	print "... ", URL(**settings.DATABASE)
	print "...above should read: "
	print "... postgresql://ebroot:42Snails@aa12jlddfw2awrj.cc6p0ojvcx3g.us-east-1.rds.amazonaws.com:5432/ebdb"
	print ".............................................."
	print "...attempting engine = create_engine(URL(**settings.DATABASE))..."
	try:
		engine = create_engine(URL(**settings.DATABASE))
		print "...Succeeded in creating engine.................."
		return engine
	except:
		print "..................................................."
		print "...Failed to create engine in database_setup.py...."
		print "..................................................."
		raise	

def makeSession():
	# Establishes a session called session which allows you to work with the DB
	try:
		print "....trying to create session.................."
		engine = db_connect()
		print "....succeeded in db_connect().................."
		Base.metadata.bind = engine
		print "....succeeded in Base.metadata.bind = engine..."
	# create a configured "Session" class
		Session = sessionmaker(bind=engine)
		print "....succeeded in Session = sessionmaker(bind=engine)..."
	# create a Session
		session = Session()
		print ".............................................."
		print "...Succeeded in creating session.............."
		print ".............................................."
		return session
	except:
		print "................................................."
		print "...Failed to create session in application.py...."
		print "................................................."
		raise	
		print "finally.... session.close()"
		session.close()
		
		
		
		
def create_tables(engine):
		Base.metadata.create_all(engine)
		
class Users(Base):
    __tablename__ = 'users'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    results = relationship("Results", cascade="all, delete-orphan")
	
    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
           'email'        : self.email,
           'password'     : self.password
       }

class Questions(Base):
    __tablename__ = "questions"
   
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    question = Column(String(250), nullable=False)
    answerA = Column(String(250), nullable=False)
    answerB = Column(String(250), nullable=False)


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'             : self.id,
           'number'         : self.number,
           'question'   : self.question,
           'answerA'    : self.scoringA,
           'answerB'    : self.scoringB
       }
 
class Results(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer,ForeignKey('users.id'))
    users = relationship(Users)
    I = Column(String(250))
    E = Column(String(250))
    N = Column(String(250))
    S = Column(String(250))
    T = Column(String(250))
    F = Column(String(250))
    J = Column(String(250))
    P = Column(String(250))

    @property
    def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'id'         	: self.id,
			'user_id'    : self.user_id,
			'I'             : self.I,
			'E'             : self.E,
			'N'             : self.N,
			'S'             : self.S,
			'T'             : self.T,
			'F'             : self.F,
			'J'             : self.J,
			'P'             : self.P
        }




