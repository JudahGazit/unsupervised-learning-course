import os

import pandas as pd

from python_code.config import PATH
from python_code.data_prep.imdb import add_imdb_raiting
from python_code.data_prep.oscars import add_oscars
from python_code.data_prep.utils import lower_columns


def load_netflix_data():
    df = pd.read_csv(os.path.join(PATH, 'netflix_titles.csv'), low_memory=False)
    return df


def prepare(df, to_list=('cast', 'country', 'listed_in', 'director'), to_lower=('title', 'director', 'cast')):
    df = df.copy()
    lower_columns(df, to_lower)
    for column in to_list:
        df[column] = df[column].str.split(', ')
    df.title = df.title.str.replace("'", "")
    df.date_added = df.date_added.str.replace('^ ', '')
    df.date_added = pd.to_datetime(df.date_added, format='%B %d, %Y')
    return df


def enrich(df, enrichers):
    df = df.copy()
    for enricher in enrichers:
        df = enricher(df)
    return df


def data_prep():
    enrichers = [add_oscars, add_imdb_raiting]
    df = load_netflix_data()
    df = prepare(df)
    df = enrich(df, enrichers)
    return df


if __name__ == '__main__':
    df = data_prep()
    df.to_json(os.path.join(PATH, 'stage.json'))
