import pandas as pd

from python_code.learning.graph.edges_logics.IEdgeLogic import IEdgeLogic


class RatingDiff(IEdgeLogic):
    def create_edges(self, df: pd.DataFrame):
        df = df.copy()
        df = df.explode('cast')
        df = df.merge(df, on=['cast'], how='left')
        df['ratingDiff'] = 10 - abs(df.averageRating_x - df.averageRating_y)
        df = df[['title_x', 'title_y', 'ratingDiff']]
        df = df[df.title_x != df.title_y]
        df = df.groupby(['title_x', 'title_y'], as_index=False).agg({'ratingDiff': 'max'})
        df.columns = ['src', 'dst', 'weight']
        return df
