from flask import render_template, request, g
from forms import LoginForm, SignUpForm
from models import *
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
	print(form.validate())
	if(request.method == 'POST' and form.validate()):
			flash('Signed Up %s ' %
				  (form.name.data))
			user = user(name, email)
			db.session.add(user)
			# db.engine.execute(""" 
			# UPDATE user()
			# """,(new_user.name, new_user.email,))
			# print(new_user.name, new_user.email)
			return redirect(url_for('/index'))
	return render_template('signup.html', title='Sign Up', form=form)
	# user = User(form.username.data, form.email.data,
                    # form.password.data)
        # db_session.add(user)
        # flash('Thanks for registering')
        # return redirect(url_for('login'))
	
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


