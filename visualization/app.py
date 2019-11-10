import os
import pickle
from flask import Flask
from flask import render_template
from tweet.tweet import Tweet

app = Flask(__name__)

ROOT_PICKLE = '../pickle/outputs/'

@app.route('/')
def index():
    pickles = os.listdir(ROOT_PICKLE)
    return render_template('index.html', pickles=pickles)

@app.route('/visualization/<pkl>')
def visualization(pkl):
    with open(os.path.join(ROOT_PICKLE, pkl), 'rb') as fd:
        post = pickle.load(fd)
    return render_template('visualization.html', post=post)
