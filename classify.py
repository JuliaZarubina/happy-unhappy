import numpy as np
from clf_loader import clf_loader
from get_vectorizer import hv

def classify(document):
    clf = clf_loader()
    label = {0: 'negative', 1: 'positive'}
    X = hv.transform([document])
    y = clf.predict(X)[0]
    proba = np.max(clf.predict_proba(X))
    return label[y], proba, clf

if __name__ == '__main__':
    classify('We love learn python')
