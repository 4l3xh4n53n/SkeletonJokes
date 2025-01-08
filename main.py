from flask import Flask, jsonify, render_template
from waitress import serve
import json
import random

app = Flask(__name__)
jokes = []


def load_jokes():
    with open('jokes/jokes.json', 'r') as file:
        d = json.load(file)
    return d


@app.route('/api', methods=['GET'])
def get_joke():
    return random.choice(data['jokes'])


@app.route('/')
def return_page():
    joke_answer = get_joke()
    return render_template('index.html', joke=joke_answer['joke'], answer=joke_answer['answer'])


data = load_jokes()
serve(app, host="0.0.0.0", port=8080)
