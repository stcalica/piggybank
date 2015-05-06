from flask import render_template, request, g, flash, redirect , url_for
from forms import LoginForm, SignUpForm
from models import User, Product, Piggybank
from app import app, db

#g stores data during the life of a request 
# can store things to sessions using session['a']
#imports the app variable 
@app.route('/')
@app.route('/index')
def index():
	products = db.engine.execute(
	""" 
	SELECT *
	FROM product
	""")
	
	return render_template('index.html')
#do form validation inside here no callback, before submitting user to database
@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignUpForm(request.form)
	if(request.method == 'POST' and form.validate_on_submit()):
			new_user = User(username=form.data['name'], email=form.data['email'])
			flash('Signed Up %s ' %
				  (form.name.data))
			db.session.add(new_user)
			db.session.commit()
			# db.engine.execute(""" 
			# UPDATE user()
			# """,(new_user.name, new_user.email,)).commit()
			# print(new_user.name, new_user.email)
			return redirect(url_for('/'))
	return render_template('signup.html', title='Sign Up', form=form)

#worry about later
#https://exploreflask.com/users.html
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if(request.method == 'POST'):
		if form.validate_submit():
			flash('Login requested for OpenID="%s", remember_me=%s' %
				  (form.openid.data, str(form.remember_me.data)))
			return redirect('/index')
	return render_template('login.html', title='Sign In', form=form)
	
#explore after login is done 
#sign in for only users that are stores 
@app.route('/add')
def add_product():
	return render_template('add_product.html', title='Add Product')
	


