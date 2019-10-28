import os
import pickle
from flask import Flask
from flask import render_template

app = Flask(__name__)

ROOT_PICKLE = '../pickle/'

@app.route('/')
def index():
    return "Mostrar pickles"

@app.route('/visualization/<pickle>')
def visualization(pickle):
    with open(os.path.join(ROOT_PICKLE, pickle), 'rb') as fd:
        json = pickle.load(fd)
    return render_template('visualization.html', json=json)