from flask import Flask, render_template, request
from sklearn.externals import joblib
import os
import numpy as np
from clf_loader import clf_loader
from most_popular_posts import most_popular_posts
from db import Comments, db_session

# import HashingVectorizer from local dir
from get_vectorizer import hv

clf = clf_loader()

def classify(document):
	label = {0: 'negative', 1: 'positive'}
	X = hv.transform([document])
	y = clf.predict(X)[0]
	proba = np.max(clf.predict_proba(X))
	return label[y], proba

app = Flask(__name__)

@app.route('/')
def index():
	pos, neg = most_popular_posts()
	return render_template('index.html', pos_posts=pos, neg_posts=neg)

#Получение тональности он-лайн, добавила секцию ниже всех твоих, Навигация - Анализ фразы

@app.route('/', methods=['POST'])
def results():
	review = request.form.get('fashionreview')
	y, proba = classify(review)
	return render_template('index.html',
		content=review,
		prediction=y,
		probability=round(proba*100, 2))

#Твои обработчики, не все поняла для чего..., все работало если даже оставить верхние два.

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


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5077)
