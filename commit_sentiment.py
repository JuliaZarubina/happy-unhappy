from clf_loader import clf_loader
from get_sentiment import get_sentiment
from db import Comments, db_session

def commit_sentiment():
    clf = clf_loader()
    scrapped_comments = Comments.query.all()
    # label = {0:'negative', 1:'positive'}
    for comment_db_row in scrapped_comments:
        current_message = comment_db_row.comment_message
        print(current_message)
        
        # current_message_preprocessed = process_message(current_message)
        # list_for_clf = []
        # list_for_clf.append(current_message_preprocessed)
        # sentiment = label[clf.predict(list_for_clf)[0]]
        sentiment = get_sentiment(current_message, clf)
        # print(sentiment)
        comment_db_row.comment_sentiment = sentiment
        # print(comment_db_row.comment_sentiment)
        db_session.add(comment_db_row)

    db_session.commit()

if __name__ == '__main__':
    commit_sentiment()
