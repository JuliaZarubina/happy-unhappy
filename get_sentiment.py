from clf_loader import clf_loader
from process_message import process_message

def get_sentiment(message_text, clf):
    label = {0:'negative', 1:'positive'}
    list_for_clf = []
    message_preprocessed = process_message(message_text)
    list_for_clf.append(message_preprocessed)
    sentiment = label[clf.predict(list_for_clf)[0]]

    return sentiment

if __name__ == '__main__':
    clf = clf_loader()
    result = get_sentiment('i love this dress')
    print(result)
