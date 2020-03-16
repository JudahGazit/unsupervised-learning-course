import networkx as nx
import pandas as pd
from sklearn.cluster import AgglomerativeClustering

from python_code.learning.clustering.ICluster import ICluster


class HierarchyClustering(ICluster):
    def __init__(self, n_clusters=100, affinity='euclidean', linkage='complete', **kwargs):
        self.cluster_engine = AgglomerativeClustering(n_clusters, affinity, linkage, **kwargs)

    def cluster(self, graph: nx.Graph):
        nodes_list = sorted(list(graph.nodes()))
        adj_matrix = nx.adj_matrix(graph, nodes_list).toarray()
        self.cluster_engine.fit(adj_matrix)
        partition = pd.DataFrame(zip(nodes_list, self.cluster_engine.labels_), columns=['title', 'community'])
        return partition
