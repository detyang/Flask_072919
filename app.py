from flask import Flask
app = Flask(__name__)

@app.route('/user/<name>')
def user_page(name):
	return '<h1>Hello User: %s</h1><img src="http://helloflask.com/totoro.gif">' %name
