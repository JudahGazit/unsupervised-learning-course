import pandas as pd

from python_code.learning.graph.edges_logics.IEdgeLogic import IEdgeLogic


class RatingDiff(IEdgeLogic):
    def create_edges(self, df: pd.DataFrame):
        """
        Creates an edge if there is a common cast member between the movies.
        The weight is the difference between the movies rank.
        Since higher score should indicate closer connection, we take the upper limit of the difference and subtract the
        difference from it.

        Example.: let movies A, B, C have the scores 5, 5.1, 6 and the cast [a, b], [c], [b]
        then the weight of the edge (A, C) would be 10-1 = 9, and the edges (A, B), (B, C) won't exist.

        :type df: pd.DataFrame
        :rtype: pd.DataFrame
        """
        df = df.copy()
        df = df.explode('cast')
        df = df.merge(df, on=['cast'], how='left')
        df['ratingDiff'] = 10 - abs(df.averageRating_x - df.averageRating_y)
        df = df[['title_x', 'title_y', 'ratingDiff']]
        df = df[df.title_x != df.title_y]
        df = df.groupby(['title_x', 'title_y'], as_index=False).agg({'ratingDiff': 'max'})
        df.columns = ['src', 'dst', 'weight']
        return df
