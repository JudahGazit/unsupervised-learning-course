import pandas as pd

from python_code.config import PATH


def is_favourite_country(countries, favourite={'United States', 'United Kingdom'}):
    if countries and isinstance(countries, list):
        return len(set(countries).intersection(favourite)) > 0
    return False


def load_df():
    df = pd.read_json(os.path.join(PATH, 'stage.json'))
    df = df[(df.type == 'Movie') & (df.averageRating >= 5) & (df.cast.isnotnull())]
    df = df[df.country.apply(is_favourite_country)]
    df.cast = df.director + df.cast
    return df
