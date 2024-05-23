import tarfile
from pathlib import Path

res = Path('/home/notjdr/dsbook/tmp/chapter-5.4/yelp_review_full_csv.tgz')
with tarfile.open(res) as tar:
    datafile = tar.extractfile('yelp_review_full_csv/train.csv')
    reviews = [line.decode('utf-8') for line in datafile]

print('\n'.join(reviews[:2]))  

