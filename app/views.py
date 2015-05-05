from flask import render_template, request, g
from forms import LoginForm
from app import app

#g stores data during the life of a request 
# can store things to sessions using session['a']
#imports the app variable 
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
	
	
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if(request.method == 'POST'):
		if form.validate_submit():
			flash('Login requested for OpenID="%s", remember_me=%s' %
				  (form.openid.data, str(form.remember_me.data)))
			return redirect('/index')
	return render_template('login.html', title='Sign In', form=form)