from sklearn.feature_extraction.text import HashingVectorizer
import re
import os
import pickle

cur_dir = os.path.dirname(os.path.abspath('__file__'))
stop = pickle.load(open(os.path.join(cur_dir, 'pkl_obj','stopwords.pkl'), 'rb'))

def tokenizer(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)',
    text.lower())
    text = re.sub('[\W]+', ' ', text.lower()) \
            + ' '.join(emoticons).replace('-', '')
    tokenized = [w for w in text.split() if w not in stop]
    return tokenized

hv = HashingVectorizer(decode_error='ignore',
                        n_features=2**21,
                        preprocessor=None,
                        tokenizer=tokenizer)
# def get_vect(tokenizer):
#     hv = HashingVectorizer(decode_error='ignore', n_features=2**21,
#                             preprocessor=None, tokenizer=tokenizer)
#     return hv

# if __name__ == '__main__':
#     document = 'I love this dress!!!'
#     print(tokenizer(document))
#     hv = get_vect(tokenizer)
#     print(hv.transform([document]))
