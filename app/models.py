from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()
""""
One user can own Multiple piggybanks
But One piggybank can only be owned by One user and linked to One product
"""
class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	store = db.Column(db.Integer)
	piggybank_id = db.Column(Integer, ForeignKey('piggybank.id')) #one to many		
	def __init__(username, email):
		self.username = username
		self.email = email
	def __repr__(self):
		return '<User %r>' % (self.username)
		
class Piggybank(db.Model):
	__tablename__ = 'piggybank'
	id = db.Column(db.Integer, primary_key=True)
	cost = db.Column(db.Integer)
	amt_paid = db.Column(db.Integer)
	earned = db.Column(db.Integer) #boolean? Finished or not
	start_date = db.Column(db.Integer) #datatime?
	end_date = db.Column(db.Integer) #datatime?
	last_payment = db.Column(db.Integer) #datatime?
	first_payment = db.Column(db.Integer) #datatime?
	name = db.Column(db.String(64), index=True, unique=True)
	product_id = db.Column(Integer, ForeignKey("product.id"))
	#owned_by_id = db.Column(Integer, ForeignKey("user.id"))
	def __init__(cost, amt_paid, earned, end_date, last_payment, product_id, email):
		self.cost = cost
		self.amt_paid = paid
		self.earned = earned
		self.end_date = end_date
		self.last_payment = last_payment
		self.product_id = product_id
		self.owned_by_id = owned_by_id
		self.email = email
		
	def __repr__(self):
		return '<User %r>' % (self.name)
		
class Product(db.Model):
	__tablename__ = 'product'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30))
	description = db.Column(db.String(100)) #may need to increase
	cost = db.Column(db.Integer)
	latest_date = db.Column(db.Integer) #datetime? latest they can hold out on
	def __init__(description, cost, lastest_date):
		self.description = description
		self.cost = cost
		self.latest_date
		
	def __repr__(self):
		return '<User %r>' % (self.name)
