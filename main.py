from flask import Flask, jsonify, request, render_template, url_for,redirect
import random
from database import add_user, add_idea, search_user, search_idea


app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

## Your code goes here! ##

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = search_user(username = username)
        if users:
            if users.password == password:
                global logged_user
                logged_user = users
                print("succ logged")
                return render_template('idea.html')

        



@app.route('/singup', methods = ['GET', 'POST'])
def singup():
    if request.method == 'GET':
        return render_template('singup.html')
        
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    user_exists = search_user(username=username)
    if not user_exists:
        add_user(username, password)
        print("succ made a user")
        return render_template('login.html')

        


@app.route('/idea', methods = ['GET', 'POST'])
def idea():
    if request.method == 'GET':
        return render_template('idea.html')
    elif request.method == 'POST':
        wyi = request.form['wyi']
        add_idea(wyi)
        return render_template('idea.html')





## And doesn't go after this line. ##

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
    debug=True
	)