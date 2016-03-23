from sqlalchemy.orm import sessionmaker
from database_setup import db_connect, create_tables

class KeirseySorterPipeline(object):
	"""KeirseySorter pipeline for storing scraped items 
	in the database"""
	def __init__(self):
		"""
		Initialize database connection and sessionmaker.
		Creates tables from database_setup
		"""
		engine = db_connect()
		create_tables(engine)
		self.Session = sessionmaker(bind=engine)
	
	def process_items(self, item, spider):
		"""
		Save data in the database
		The method is called for every item pipeline component.
		"""
		session = self.Session()
		deal = Deals(**item)
		
		try:
			session.add(dataEntry)
			session.commit()
		except:
			session.rollback()
			raise
		finally:
			session.close()
		
		return item
	

