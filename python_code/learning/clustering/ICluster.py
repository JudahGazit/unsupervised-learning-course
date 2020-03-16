import networkx as nx
import pandas as pd


class ICluster(object):
    def cluster(self, graph: nx.Graph):
        """
        :type graph: nx.Graph
        :rtype: pd.DataFrame
        """
        raise NotImplementedError()
