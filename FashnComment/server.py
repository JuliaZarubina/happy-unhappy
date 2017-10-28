from flask import Flask, abort, request, render_template
from jinja2 import Template
import requests
#from flask_inputs.validators import JsonSchema

app = Flask(__name__)


	
@app.route('/')
def XOXO():
    return render_template('XOXO.html')
	
@app.route('/')
def main_form():
    return '<form action="submit" id="textform" method="post"><textarea name="text">Hello World!</textarea><input type="submit" value="Submit"></form>'

@app.route('/submit', methods=['POST'])
def submit_textarea():
    return "You entered: {}".format(request.form["text"])

@app.route('/addRegion', methods=['POST'])
def addRegion():
    print(request.form['projectFilepath'])

@app.route('/static/style.css')
def send_css(path):
    return send_from_directory('static', path)
	
@app.route('/users', methods=['POST'])
def create_user():
   print("Got Post Info")
   name = request.form['name']
   DojoLocation = request.form['location']
   FavoriteLanguage = request.form['Language']
   textarea = request.form['textarea']
   # redirects back to the '/' route
   return render_template('bk.html')
	

if __name__ == "__main__":
    app.run()