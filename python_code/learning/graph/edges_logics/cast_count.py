from python_code.learning.graph.edges_logics.IEdgeLogic import IEdgeLogic


class CastCount(IEdgeLogic):
    def create_edges(self, df):
        """
        this class creates naive edges between movies with common cast.
        the weight of the edge is the number of common cast members between the movies.
        :param df: pd.DataFrame
        :returns pd.DataFrame
        """
        df = df.copy()
        df = df.explode('cast')
        df = df.merge(df, on=['cast'], how='left')
        df = df[['title_x', 'title_y', 'cast']]
        df = df[df.title_x != df.title_y]
        df = df.groupby(['title_x', 'title_y'], as_index=False).agg({'cast': 'count'})
        df.columns = ['src', 'dst', 'weight']
        return df
