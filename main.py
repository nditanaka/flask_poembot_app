import time
from flask import Flask, request, render_template, jsonify, make_response
from poemBot import tap, getURL
from bs4poems import getbs4Poems

app = Flask(__name__)


@app.route('/')
def index():
    # title, author, poem, years, url = tap()
    bs4poem = getbs4Poems()
    title, author, date, poem, url = bs4poem[0], bs4poem[1], bs4poem[2], bs4poem[3], bs4poem[4]
    # [title, author, date, poem, url]
    headers = {'Content-Type': 'text/html'}
    return make_response(render_template('index.html', title=title, author=author, date=date, poem=poem, url=url), 200, headers)


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/api/about')
def about():
    return 'This is the about page'


@app.route('/api/poem')
def get_random_poem():
    return tap()
