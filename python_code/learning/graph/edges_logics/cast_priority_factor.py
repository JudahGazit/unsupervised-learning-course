from python_code.learning.graph.edges_logics.IEdgeLogic import IEdgeLogic


class CastPriorityFactor(IEdgeLogic):
    def create_edges(self, df):
        """
        This class creates edges between movies with common actors.
        Assuming the order of the cast members in the list indicates their importance to the movie,
        we give each of them a weight: the first gets 1, the second gets 0.5, the third gets 0.25 and so on.
        The weight of the edge between x and y is the sum of the weights of the common actors in both movies.

        Example:
        Movie x cast: ['a', 'b', 'c']
        Movie y cast: ['a', 'c', 'd']
        the weight of the edge (x, y) is 1 + 1 + 0.5 + 0.25 = 2.75

        :type df: pd.DataFrame
        :rtype pd.DataFrame
        """
        df = df.copy()
        df = df[df.cast.apply(lambda l: isinstance(l, list))]
        df = self.__explode_cast_with_factors(df)
        df = df.merge(df, on=['cast'], how='left')
        df['cast_factor'] = df.cast_factor_x + df.cast_factor_y
        df = df[df.title_x != df.title_y].groupby(['title_x', 'title_y'], as_index=False) \
            .agg({'cast_factor': 'sum'})
        df.columns = ['src', 'dst', 'weight']
        return df

    def __explode_cast_with_factors(self, df):
        df.cast = df.cast.apply(lambda l: [(2 ** (-i), x) for i, x in enumerate(l)])
        df = df.explode('cast')
        df['cast_factor'] = df.cast.apply(lambda t: t[0] if t is not None else None)
        df.cast = df.cast.apply(lambda t: t[1] if t is not None else None)
        return df
