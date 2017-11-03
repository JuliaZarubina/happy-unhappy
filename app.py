from flask import Flask, redirect, url_for, render_template, request
from most_popular_posts import most_popular_posts
from db import Comments, db_session
from classify import classify
from check_page import check_page
from online_fb_scrape import online_scrape
from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


SECRET_KEY = "asdfhjgfdsyuhgfcxdsrethgf"
DEBUG = False
WTF_CSRF_ENABLED = True

class FBForm(FlaskForm):
    fb_name = StringField('Name:', validators=[validators.required()])

class PhraseForm(FlaskForm):
    user_phrase = StringField('Phrase:', validators=[validators.required()])

app = Flask(__name__)
app.config.from_object(__name__)
error_text = 'The page you requested can not be found.'


@app.route('/', methods=['GET','POST'])
def index():
    fb_page_form = FBForm()
    user_phrase_form = PhraseForm()
    pos_posts, neg_posts = most_popular_posts() 

    if fb_page_form.validate_on_submit():
        user_input = fb_page_form.fb_name.data
        fb_page = check_page(user_input)
        if not fb_page:
            error = error_text
            return error
        else:   
            total, pos, neg = online_scrape(fb_page)

        return render_template('index.html',
                                total=total,
                                pos=pos,
                                neg=neg,
                                error=error,
                                pos_posts=pos_posts,
                                neg_posts=neg_posts,
                                fb_page_form=fb_page_form,
                                user_phrase_form=user_phrase_form)

    if user_phrase_form.validate_on_submit(): 
        phrase = user_phrase_form.user_phrase.data
        y, proba, clf = classify(phrase)
        prob = round(proba*100, 2)

        return render_template('index.html',
                                content=phrase,
                                prediction=y,
                                probability=prob,
                                pos_posts=pos_posts,
                                neg_posts=neg_posts,
                                user_phrase_form=user_phrase_form,
                                fb_page_form=fb_page_form)


    return render_template('index.html',
                            pos_posts=pos_posts,
                            neg_posts=neg_posts,
                            fb_page_form = fb_page_form,
                            user_phrase_form=user_phrase_form)	

if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0', port=5077)
