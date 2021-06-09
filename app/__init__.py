import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about/ishika')
def about_ishika():
    return render_template('about_base.html', fellowName='Ishika');

@app.route('/about/frankie')
def about_frankie():
    return render_template('about_base.html', fellowName='Frankie');

@app.route('/about/sebastian')
def about_sebastian():
    return render_template('about_base.html', fellowName='Sebastian');