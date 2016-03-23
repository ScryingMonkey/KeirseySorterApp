from flask import Flask, render_template, request, redirect,jsonify, url_for, flash

import sqlalchemy
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Users, Questions, Results

from flask import session as login_session
import random, string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

from database_setup import db_connect, makeSession, create_tables, Base, Questions
import settings

# EB looks for an 'application' callable by default.
application = Flask(__name__)
session = makeSession()

#.............................................................................................
#.....Helper functions.............................................................................
#.............................................................................................

# Takes in a dictionary of results (question1=a, question2=b, etc)
# Returns a dictionary of scores for each personality aspect (ex. N = 18)
def scoreResults(results):
	print "...In scoreResults............"
	scores = {'e':0, 'i':0, 's':0, 'n':0, 't':0, 'f':0, 'j':0, 'p':0}
	personalities = ['z','e','i','s','n','s','n','t','f','t','f','j','p','j','p']
	print "...before scoring: %s ................." % scores
	for x in range(0,9): #<-----------------------this must be corrected to 0,10 once the db is corrected to have 70 questions
		for i,a in enumerate(range(1,14,2)):
			b = a+1
			#print i+1+x*7,a,b
			if results[i+1+x*7] == 'a':
				scores[personalities[a]] += 1
			elif results[i+1+x*7] == 'b':
				scores[personalities[b]] += 1
			else:
				print "...ERROR in scoreResutls(): Invalid input on question %s ............." % str(n+7*x)
	print "...after scoring: %s ..............." % scores
	
	return scores


#.............................................................................................
#.....GET Requests.............................................................................
#.............................................................................................

# test html
@application.route('/')
@application.route('/testApp')
def testApp():
	return render_template('testing00.html')

# test engine connection
@application.route('/testEngine')
def testEngine():
	print "Entering test()"
	session = makeSession()
	#Retrieve first question from database
	questions = session.query(Questions).all()
	testQuestions = [{'name': 'First', 'question': questions[0]}, {'name': 'Last', 'question': questions[-1]}]
	print "..........First & last questions..."
	for q in testQuestions:
		print ".............................................."
		#print "Printing % question.................." % q['name']
		print q['name']
		print q['question'].number, "...", q['question'].question, " : ", q['question'].answerA, " or ", q['question'].answerB
		#print q.question.number, "...", q.question.question, " : ", q.question.answerA, " or ", q.question.answerB
		print ".............................................."
	print "...Success...................................."
	print ".............................................."
	return render_template('questions.html')

# Show all Questions
@application.route('/questions')
def showQuestions():
	questions = session.query(Questions).order_by(Questions.number)
	return render_template('questions.html', questions=questions)

# Pull all stored results from database and display them
@application.route('/allResults')
def showAllScores():
	scores = session.query(Results).all()
	for score in scores:
		print score
	return render_template('allScores.html', scores=scores)
	
#.............................................................................................
#.....GET Requests.............................................................................
#.............................................................................................

# Show results
@application.route('/results', methods=['GET','POST'])
def showResults():
	print "...In showResults().................."
	if request.method == 'POST':
		#print "...in /results if POST......"
		results = {}
		for n in range(1,69):
			result = "result" + str(n)	
			#print result
			results.update({n:str(request.form[result])})
		print results
		# send dictionary results, returns dictionary scores
		scores = scoreResults(results)	
		# ToDo: Include user in commit in order to store results by user using Oauth2
		newResults = Results(I = scores['i'],
							E = scores['e'],
							N = scores['n'],
							S = scores['s'],
							T = scores['t'],
							F = scores['f'],
							J = scores['j'],
							P = scores['p'],)
		#user_id=login_session['user_id'])
		session.add(newResults)
		#flash('New Menu %s Item Successfully Created' % (newItem.name))
		flash('New Results Successfully Saved')
		session.commit()
		print "...session sucessfully committed.........."
		return render_template('results.html', scores = scores)
	else:
		return render_template('questions.html')
	
#.............................................................................................
#.....Boiler plate.............................................................................
#.............................................................................................			

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
	application.secret_key = 'super_secret_key'
	#application.debug = True
	application.run()
	#application.run(host = '0.0.0.0', port = 5000)
