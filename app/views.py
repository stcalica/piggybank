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
	
@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignUpForm(request.form)
	if(request.method == 'POST' and form.validate()):
			print(form.data)
			print(form.data['name'])
			print(form.data['email'])
			new_user = User(username=form.data['name'], email=form.data['email'])
			flash('Signed Up %s ' %
				  (form.name.data))
			db.session.add(new_user)
			db.session.commit()
			# db.engine.execute(""" 
			# UPDATE user()
			# """,(new_user.name, new_user.email,))
			# print(new_user.name, new_user.email)
			return render_template('index.html')
	return render_template('signup.html', title='Sign Up', form=form)

	
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if(request.method == 'POST'):
		if form.validate_submit():
			flash('Login requested for OpenID="%s", remember_me=%s' %
				  (form.openid.data, str(form.remember_me.data)))
			return redirect('/index')
	return render_template('login.html', title='Sign In', form=form)
	
#sign in for only users that are stores 
@app.route('/add_product')
def add_product():
	return render_template('add_product.html', title='Add Product')


