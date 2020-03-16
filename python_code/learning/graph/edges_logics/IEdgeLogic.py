import pandas as pd


class IEdgeLogic(object):
    def create_edges(self, df: pd.DataFrame):
        """
        Returns a dataframe of edges: [src, dst, weight]
        :type df: pd.DataFrame
        :rtype: pd.DataFrame
        """
        raise NotImplementedError
