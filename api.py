import time
from flask import Flask, request, render_template, jsonify
from poemBot import tap

app = Flask(__name__)


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/api/about')
def about():
    return 'This is the about page'


@app.route('/api/poem')
def get_random_poem():
    return tap()


def execute():
    return tap()


output = execute()
# print(output)


# @app.route('/lower', methods=["GET", "POST"])
# def lower_case():
#     text1 = request.form['text']
#     word = text1.lower()
#     result = {
#         "result": word
#     }
#     result = {str(key): value for key, value in result.items()}
#     return jsonify(result=result)
