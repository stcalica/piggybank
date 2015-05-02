from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()



class Products(Base):
	__tablename__ = 'products'
	id = Column(Integer, primary_key = True)
	name = Column(String(100))



class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key = True)

	name = Column(String(100))


class Piggybank(Base):
	__tablename__ = 'piggybank' 
	id = Column(Integer, primary_key = True)
	name = Column(String(100))







#create engine and point to the database we will use 

engine = create_engine('postgresql://Digibank.db')
Base.metadata.create_all(engine)