import networkx as nx


class ICluster(object):
    def cluster(self, graph: nx.Graph):
        """
        :type graph: nx.Graph
        :rtype: pd.DataFrame
        """
        raise NotImplementedError()
