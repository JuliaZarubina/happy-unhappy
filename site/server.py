from flask import Flask, abort, request, render_template
from jinja2 import Template
import requests

app = Flask(__name__)

@app.route('/')
def XOXO():
    return render_template('XOXO.html')

@app.route('/addRegion', methods=['POST'])
def addRegion():
    print(request.form['projectFilepath'])

@app.route('/static/style.css')
def send_css(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run()