import os

BOT_NAME = 'keirseysorter'

SPIDER_MODULES = ['keirseysorter.project']

if 'RDS_HOSTNAME' in os.environ:
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
	DATABASE = {
    'drivername': 'postgresql',
    'host': 'aahzr3iq8swjzx.cc6p0ojvcx3g.us-east-1.rds.amazonaws.com',
    'port': '5432',
    'username': 'datadude',
    'password': '42Snails',
    'database': 'ebdb'
	}
ITEM_PIPELINES = ['keirseysorter.pipeline.KeirseySorterPipeline']
