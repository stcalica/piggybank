from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
#one to many with piggybanks

    def __repr__(self):
        return '<User %r>' % (self.username)
		
class Piggybank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
	cost = db.Column(db.Integer)
	amt_paid = db.Column(db.Integer)
	earned = db.Column(db.Integer) #boolean? Finished or not
	start_date = db.Column(db.Integer) #datatime?
	end_date = db.Column(db.Integer) #datatime?
	last_payment = db.Column(db.Integer) #datatime?
	first_payment = db.Column(db.Integer) #datatime?
    name = db.Column(db.String(64), index=True, unique=True)
#one to one with user
#one to one with product
    def __repr__(self):
        return '<User %r>' % (self.name)
		
class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30))
	description = db.Column(db.String(100)) #may need to increase
	cost = db.Coulmn(db.Integer)
	latest_date = db.Coulmn(db.Integer) #datetime? latest they can hold out on
	 def __repr__(self):
        return '<User %r>' % (self.name)
