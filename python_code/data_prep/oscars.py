import pandas as pd

from python_code.config import PATH


def load_oscars():
    df = pd.read_csv(PATH + 'oscars.csv')
    return df


def prepare_oscars(oscars):
    oscars = oscars.copy()
    oscars.win = oscars.win.apply(lambda value: 1 if value else 0)
    oscars.film = oscars.film.str.lower()
    oscars = oscars[(oscars.film != ' ') & (oscars.film.notnull())].groupby(['film'], as_index=False).agg(
        {'win': 'sum'})
    oscars['title'] = oscars.film.str.replace("'", '')
    oscars = oscars[['title', 'win']]
    return oscars


def add_oscars(df):
    oscars = load_oscars()
    oscars = prepare_oscars(oscars)
    oscars['type'] = 'Movie'
    df = df.merge(oscars, on=['title', 'type'], how='left')
    df.win = df.win.apply(lambda value: value if value is not None else 0)
    return df
