from flask import Flask, redirect, url_for, render_template, request
from most_popular_posts import most_popular_posts
from db import Comments, db_session
from classify import classify
from online_fb_scrape import online_scrape
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

SECRET_KEY = "asdfhjgfdsyuhgfcxdsrethgf"
DEBUG = True
# app.config['SECRET_KEY'] = b'\x97\xff\x83\xf6\x7f\x00lQ]\xc5r\ry9\xdd\r%j\x06\x0e\x1cJ\x84\xc6'

class ReusableForm(Form):
    name = StringField('Name:', validators=[validators.required()])

app = Flask(__name__)
app.config.from_object(__name__)
    
@app.route('/', methods=['GET','POST'])
def index():
  if request.method == 'GET':
    pos_posts, neg_posts = most_popular_posts()
  
    return render_template('index.html',
                          pos_posts=pos_posts,
                          neg_posts=neg_posts)

  form = ReusableForm()
  if 'fb_name' in request.form and form.validate():
    fb_page = request.form.get('fb_name')
    total, pos, neg = online_scrape(fb_page)

    return render_template('index.html',
                            _anchor='scrape',
                            total=total,
                            pos=pos,
                            neg=neg,
                            form=form)
      
  # elif 'phrase' in request.form: 
  #   review = request.form.get('phrase')
  #   y, proba, clf = classify(review)

  #   return render_template('index.html',
  #                       _anchor='result', 
  #                       content=review,
  #                       prediction=y,
  #                       probability=round(proba*100, 2))

# TODO
# @app.route('/')
# def main_form():
#     return '<form action="submit" id="textform" method="post"><textarea name="text">Hello World!</textarea><input type="submit" value="Submit"></form>'

# @app.route('/submit', methods=['POST'])
# def submit_textarea():
#     return "You entered: {}".format(request.form["text"])

# @app.route('/addRegion', methods=['POST'])
# def addRegion():
#     print(request.form['projectFilepath'])

# @app.route('/static/style.css')
# def send_css(path):
#     return send_from_directory('static', path)
	
# @app.route('/users', methods=['POST'])
# def create_user():
#    print("Got Post Info")
#    name = request.form['name']
#    DojoLocation = request.form['location']
#    FavoriteLanguage = request.form['Language']
#    textarea = request.form['textarea']
#    # redirects back to the '/' route
#    return render_template('bk.html')	


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5077)
