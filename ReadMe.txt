

Objective: Let users login with unique IDs.  Present questions from a database
 of questions.  Record user answers in a database.  Score user answers and save 
the scores from each survey with a reference to the user's ID.

Database{
	Users{
		userID: int primary key
		name: string
		password: string
	}		
	Questions{
		id: int primary key
		number: int
		question: string
		answerA: string
		answerB: string
	}
	Results{
		testID: int primary key
		userID: foreign key
		I: int
		E: int
		N: int
		S: int
		T: int
		F: int
		J: int
		P: int
	}
}

pg_config file will configure a vagrant machine to be prepared to deploy to Heroku.
