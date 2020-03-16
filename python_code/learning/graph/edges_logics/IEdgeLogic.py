import pandas as pd


class IEdgeLogic(object):
    def create_edges(self, df: pd.DataFrame):
        """
        Returns a dataframe of edges: [src, dst, weight]
        :param df: pd.DataFrame
        """
        raise NotImplementedError
