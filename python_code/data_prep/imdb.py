import pandas as pd

from python_code.config import PATH
from python_code.data_prep.utils import lower_columns


def load_imdb():
    titles = pd.read_csv(PATH + 'title.basics.tsv', sep='\t')
    raiting = pd.read_csv(PATH + 'title.ratings.tsv', sep='\t')
    df = titles.merge(raiting, on=['tconst'])
    return df


def prepare_imdb(imdb, to_lower=['primaryTitle', 'originalTitle'], to_keep=['averageRating', 'numVotes']):
    imdb = imdb.copy()
    lower_columns(imdb, to_lower)
    imdb = imdb[to_lower + to_keep]
    imdb['title'] = imdb.primaryTitle.str.replace("'", '')
    imdb.averageRating = imdb.averageRating * imdb.numVotes
    imdb = imdb.groupby(['title'], as_index=False).agg({'averageRating': 'sum', 'numVotes': 'sum'})
    imdb.averageRating = imdb.averageRating / imdb.numVotes
    return imdb


def add_imdb_raiting(df):
    imdb = load_imdb()
    imdb = prepare_imdb(imdb)
    imdb.title = imdb.title.str.replace('&', 'and')
    df.title = df.title.str.replace('&', 'and')
    df = df.merge(imdb, on=['title'], how='left')
    return df
