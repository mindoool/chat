import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import pusher
import json


app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key='smlwy'

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
p = pusher.Pusher(
	app_id='83091',
	key='4e1da9ef46b3a8d5088e',
	secret='7946287f2b256b605d45'
	)

@app.route('/')
def index():
	if 'username' in session:
		return render_template('index.html')
	else:
		return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method =="POST":
		session['username'] = request.form['username']
		p['my_channel'].trigger('notification',{"username":session['username']})
		# return render_template("chat.html")
		return render_template("index.html")
	else:
		return render_template("login.html")

@app.route('/chat',methods=['GET','POST'])
def chat():
	if request.method=='POST':
		p['my_channel'].trigger('chat', {"username":session['username'],"chat":request.form['chat']})
		valid['content']='ok'
		return json.dumps(valid)
		# return render_template('chat.html')
	else:
		valid['content']=session['username']
		return json.dumps(valid)
	return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

