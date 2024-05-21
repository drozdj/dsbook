import tarfile
from itertools import islice
from metaflow import S3
from pathlib import Path


def load_yelp_reviews(num_docs):
    res = Path('/home/notjdr/dsbook/chapter-5/yelp_review_full_csv.tgz')
    with tarfile.open(res) as tar:
        datafile = tar.extractfile('yelp_review_full_csv/train.csv')
        return list(islice(datafile, num_docs))

def make_matrix(docs, binary=False):
    from sklearn.feature_extraction.text import CountVectorizer
    vec = CountVectorizer(min_df=10, max_df=0.1, binary=binary)
    mtx = vec.fit_transform(docs)
    cols = [None] * len(vec.vocabulary_)
    for word, idx in vec.vocabulary_.items():
        cols[idx] = word
    return mtx, cols
