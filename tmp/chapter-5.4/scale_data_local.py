from itertools import islice
from pathlib import Path
import tarfile


def load_yelp_reviews(num_docs, file_path):
    with tarfile.open(file_path, 'r:gz') as tar:
        datafile = tar.extractfile('yelp_review_full_csv/train.csv')
        return list(islice((line.decode('utf-8').strip() for line in datafile), num_docs))

def make_matrix(docs, binary=False):
    from sklearn.feature_extraction.text import CountVectorizer
    vec = CountVectorizer(min_df=10, max_df=0.1, binary=binary)
    mtx = vec.fit_transform(docs)
    cols = [None] * len(vec.vocabulary_)
    for word, idx in vec.vocabulary_.items():
        cols[idx] = word
    return mtx, cols
