from flask import Flask, render_template
app = Flask(__name__)

name = 'Det Yang'
movies = [
    {'title': 'Titanic', 'year': '1997'},
    {'title': 'The Prestige', 'year': '2006'},
    {'title': 'Nightcrawler', 'year': '2014'},
    {'title': 'The Secret Life of Walter Mitty', 'year': '2013'},
    {'title': 'Three Billboards', 'year': '2018'},
    {'title': 'Up', 'year': '2009'},
    {'title': 'The Hateful Eight', 'year': '2015'},
    {'title': 'Big Fish', 'year': '2003'},
    {'title': 'The Sixth Sense', 'year': '1999'}
]

@app.route('/')
def index():
        return render_template('index.html', name=name, movies=movies)

