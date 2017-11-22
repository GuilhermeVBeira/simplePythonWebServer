from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Person(Base):
	__tablename__ = 'person'
	id = Column(Integer, primary_key=True)
	firstname = Column(String(100), nullable=False)
	lastname = Column(String(100), nullable=False)
	adress = Column(String(100), nullable=False)

	def __repr__(self):
		return self.firstname
	
class DataBase:
	def __init__(self, DataBase):
		self.database = DataBase
		engine = create_engine(self.database )
		# Base.metadata.create_all(engine)
		Session = sessionmaker(bind=engine)
		self.session = Session()
		self.session.commit()

	def boot_database(self):
		engine = create_engine(self.database)
		Base.metadata.create_all(engine)
	