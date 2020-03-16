import networkx as nx
import pandas as pd
import sklearn

from python_code.learning.ICluster import ICluster


class SpectralClustering(ICluster):
    def __init__(self, n_clusters=100, **kwargs):
        self.cluster_engine = sklearn.cluster.SpectralClustering(n_clusters, **kwargs)

    def cluster(self, graph: nx.Graph):
        nodes_list = sorted(list(graph.nodes()))
        adj_matrix = nx.adj_matrix(graph, nodes_list).toarray()
        self.cluster_engine.fit(adj_matrix)
        partition = pd.DataFrame(zip(nodes_list, self.cluster_engine.labels_), columns=['title', 'community'])
        return partition
