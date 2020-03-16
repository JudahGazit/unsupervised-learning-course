import networkx as nx
import pandas as pd
import sknetwork as skn

from python_code.learning.ICluster import ICluster


class Louvain(ICluster):
    def __init__(self, resolution=30):
        self.louvain = skn.clustering.Louvain('python', resolution=resolution, random_state=None)

    def cluster(self, graph: nx.Graph):
        nodes_list = sorted(list(graph.nodes()))
        self.louvain.fit(nx.adj_matrix(graph, nodes_list))
        partition = pd.DataFrame(zip(nodes_list, self.louvain.labels_), columns=['title', 'community'])
        return partition
