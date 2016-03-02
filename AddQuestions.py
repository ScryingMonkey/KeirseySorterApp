
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Users, Questions, Results, Base
 
engine = create_engine('sqlite:///MBTestingDatabase.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

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

#Gather questions from txt file
questions = CollectQuestions("static\Keirsey_Sorter.txt")
print questions

#Add questions to database
for q in questions:
    question = Questions(number = q['number'],
                          question = q['question'],
                          answerA = q['answerA'],
                          answerB = q['answerB'] )
    print "%s. %s..." %(q['number'], q['question'])
    
    session.add(question)
    session.commit()
