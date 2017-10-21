from clf_loader import clf_loader
from get_sentiment import get_sentiment
from db import Comments, db_session

def commit_sentiment():
    clf = clf_loader()
    scrapped_comments = Comments.query.all()
    for comment_db_row in scrapped_comments:
        current_message = comment_db_row.comment_message
        sentiment = get_sentiment(current_message, clf)
        comment_db_row.comment_sentiment = sentiment
        db_session.add(comment_db_row)

    db_session.commit()

if __name__ == '__main__':
    commit_sentiment()
