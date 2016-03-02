from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

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
    __tablename__ = 'questions'
   
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



engine = create_engine('sqlite:///MBTestingDatabase.db')
 

Base.metadata.create_all(engine)
