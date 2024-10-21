from flask import Flask, jsonify, render_template
from waitress import serve

import json
import random

app = Flask(__name__)
jokes = []


def load():
    with open('jokes/jokes.json', 'r') as file:
        data = json.load(file)

    for joke in data['jokes']:
        jokes.append(joke)

    return jokes


@app.route('/api', methods=['GET'])
def get_joke():
    return jsonify(random.choice(jokes))


@app.route('/')
def return_page():
    joke_answer = random.choice(jokes)
    return render_template('index.html', joke=joke_answer['joke'], answer=joke_answer['answer'])


load()
serve(app, host="0.0.0.0", port=8080)
