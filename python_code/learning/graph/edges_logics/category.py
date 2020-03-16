from python_code.learning.graph.edges_logics.IEdgeLogic import IEdgeLogic


class CastPriorityFactor(IEdgeLogic):
    def create_edges(self, df):
        """
        This class creates edges between movies with common categories.
        The weight is set by the amount of common categories between the movies.
        :param df: pd.DataFrame
        :returns pd.DataFrame
        """
        df = df.copy()
        df = df.explode('listed_in')
        df = df.merge(df, on=['listed_in'], how='left')
        df = df[df.title_x != df.title_y].groupby(['title_x', 'title_y'], as_index=False).agg({'listed_in': 'count'})
        df.columns = ['src', 'dst', 'weight']
        return df
