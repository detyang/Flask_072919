import os
import sys
import click

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template


WIN = sys.platform.startswith('win')
if WIN:
	prefix = 'sqlite:///'
else:
	prefix = 'sqlite:////'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))



@app.cli.command()
def forge():
    db.create_all()

    name = 'Det Yang'
    movies = [
        {'title': 'Titanic', 'year': '1997'},
        {'title': 'The Prestige', 'year': '2006'},
        {'title': 'The Sixth Sense', 'year': '1999'},
        {'title': 'Up', 'year': '2009'},
        {'title': 'Nightcrawler', 'year': '2014'},
        {'title': 'The Secret Life of Walter Mitty', 'year': '2013'},
        {'title': 'Identity', 'year': '2003'},
        {'title': 'Three Billboards', 'year': '2017'},
        {'title': 'Dogvile', 'year': '2004'},
    ]
    
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')

def initdb(drop):
    """Initialize the database"""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')



@app.route('/')
def index():
    user = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html', user=user, movies=movies)
