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
	session = makeSession()
	print "...makeSession() successful......"
	questions = session.query(Questions).order_by(Questions.number)
	return render_template('questions.html', questions=questions)
	
#.............................................................................................
#.....GET Requests.............................................................................
#.............................................................................................

# Show results
@application.route('/results', methods=['GET','POST'])
def showResults():
	if request.method == 'POST':
		newResults = Results(name = request.form['name'],
		user_id=login_session['user_id'])
		session.add(newResults)
		flash('New Results Successfully Saved')
		session.commit()
		return render_template('questions.html')	  
	else:
		return redirect(url_for('results'))
	
#.............................................................................................
#.....Boiler plate.............................................................................
#.............................................................................................			

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #application.debug = True
    application.run()
    #application.run(host = '0.0.0.0', port = 5000)
