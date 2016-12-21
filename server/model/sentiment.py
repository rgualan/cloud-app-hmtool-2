import csv
import re
from server.settings import *

def get_test_data():
    file_path = PROJECT_DIR+'/../data/brexit.csv'
    delimiter = str(';')

    csvfile = open(file_path, 'r')
    csv.register_dialect(
        'dataset',
        delimiter = delimiter,)
    reader = csv.DictReader(csvfile, dialect='dataset')

    results = []
    for tweet in reader:
        sentence = tweet['tweetext'].split()
        for word in sentence:
            h = re.match('(.*)http.*$', word)
            u = re.match('(.*)\.com.*$', word)
            if h is None and u is None:
                chars_to_remove = ['"', '!', '#', '.', '?', '@', ':', '\'s', '~']
                subj = word
                word = subj.translate(None, ''.join(chars_to_remove))
                results.append(word)
            else:
                pass

    return results
