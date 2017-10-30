import os
import pickle
from sklearn.externals import joblib

def clf_loader():
    BASE_DIR = os.path.dirname(os.path.abspath('__file__'))
    pkl_obj_path = os.path.join(BASE_DIR, 'pkl_obj')
    clf = joblib.load(open(os.path.join(pkl_obj_path,'sgdClassifier.pkl'), 'rb'))

    return clf

if __name__ == '__main__':
    result = clf_loader()
    print(result)

