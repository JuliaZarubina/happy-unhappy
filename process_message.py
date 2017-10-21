import re
import csv
import string

def process_message(message):
    # process the tweets

    #convert to lower case
    message = message.lower()  
    #remove www.* or https?://* 
    message = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http[^\s]+))',' ',message)
    #remove @username
    message = re.sub('@[^\s]+',' ',message)
    #remove additional white spaces
    message = re.sub('[\s]+', ' ', message)
    #remove digits
    message = re.sub('[0-9]', ' ', message)
    #latin
    message = re.sub('[\p{Latin}\p{posix_punct}]abc?','',message)
    #remove punctuation
    translation = str.maketrans('','', string.punctuation)
    message = message.translate(translation)
    #Replace #word with word
    message = re.sub(r'#([^\s]+)', r'\1', message)
    # message = tweet.strip('\'"')
    message = message.strip()

    return message
