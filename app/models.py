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
    address = Column(String(100), nullable=False)

    def __repr__(self):
        return self.firstname


class DataBase:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.session.commit()

    def boot(self):
        Base.metadata.create_all(self.engine)