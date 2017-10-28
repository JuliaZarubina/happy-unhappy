from flask import Flask, render_template, request
from sklearn.externals import joblib
import os
import numpy as np
from clf_loader import clf_loader
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
	comments = Comments.query.all()
	return render_template('index.html', comments=comments)

@app.route('/sentiment')
def sentiment():
	return render_template('sentiment.html')

@app.route('/results', methods=['POST'])
def results():
	review = request.form.get('fashionreview')
	y, proba = classify(review)
	return render_template('results.html',
		content=review,
		prediction=y,
		probability=round(proba*100, 2))


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5077)
