import networkx as nx
import pandas as pd
import sknetwork as skn

from python_code.learning.clustering.ICluster import ICluster


class Louvain(ICluster):
    def __init__(self, resolution=60, **kwargs):
        self.cluster_engine = skn.clustering.Louvain('python', resolution=resolution, random_state=None, **kwargs)

    def cluster(self, graph: nx.Graph):
        nodes_list = sorted(list(graph.nodes()))
        self.cluster_engine.fit(nx.adj_matrix(graph, nodes_list))
        partition = pd.DataFrame(zip(nodes_list, self.cluster_engine.labels_), columns=['title', 'community'])
        return partition