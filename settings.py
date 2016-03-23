import os

BOT_NAME = 'keirseysorter'

SPIDER_MODULES = ['keirseysorter.project']

print "...in settings.py......."
"""if 'RDS_HOSTNAME' in os.environ:
	print "...in settings if...."
	DATABASE = {
		'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
	print "...in else settings.py....."
	DATABASE = {
		'drivername': 'postgresql',
		'username': 'ebroot',
		'password': '42Snails',
		'database': 'ebdb',
		'host': 'aa12jlddfw2awrj.cc6p0ojvcx3g.us-east-1.rds.amazonaws.com',
		'port': '5432',
	}
"""
DATABASE = {
	#'drivername': 'postgresql',
	'drivername': 'postgresql+psycopg2',
	'username': 'ebroot',
	'password': '42Snails',
	'database': 'ebdb',
	'host': 'aa12jlddfw2awrj.cc6p0ojvcx3g.us-east-1.rds.amazonaws.com',
	'port': '5432',
	}


ITEM_PIPELINES = ['keirseysorter.pipeline.KeirseySorterPipeline']
