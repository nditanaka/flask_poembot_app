import time
from flask import Flask, request, render_template, jsonify
from poemBot import tap

app = Flask(__name__)


@app.route('/')
def index():
    title, author, poem, years, url = tap()
    return render_template('index.html', title=title, author=author, poem=poem, years=years, url=url)


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/api/about')
def about():
    return 'This is the about page'


@app.route('/api/poem')
def get_random_poem():
    return tap()
