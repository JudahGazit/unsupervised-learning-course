import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from sklearn import manifold
from sklearn.cluster import DBSCAN

from python_code.learning.ICluster import ICluster


class MDSClustering(ICluster):
    def __init__(self, dimensions=2, metric=True, clusters=8, **kwargs):
        self.mds = manifold.MDS(2, metric=True, **kwargs)
        self.kmeans = DBSCAN(0.5)

    def cluster(self, graph: nx.Graph, draw_results=True):
        nodes_list = sorted(list(graph.nodes()))
        adj_matrix = nx.adj_matrix(graph, nodes_list).toarray()
        transformed = self.transform(adj_matrix)
        partition = self.partition_transformed(transformed)
        partition = pd.DataFrame(zip(nodes_list, transformed, partition), columns=['title', 'xy', 'community'])
        if draw_results:
            self.draw_partitions(partition)
        return partition

    def partition_transformed(self, transformed):
        partition = self.kmeans.fit_predict(transformed)
        return partition

    def transform(self, adj_matrix):
        transformed = self.mds.fit_transform(adj_matrix)
        return transformed

    def draw_transformed(self, transformed):
        plt.scatter([_[0] for _ in transformed], [_[1] for _ in transformed])
        plt.show()

    def draw_partitions(self, partition):
        partition_grouped = partition.groupby(['community'])
        partition_grouped.xy = partition_grouped.xy.apply(list)
        for v in partition_grouped.xy.values:
            plt.scatter([_[0] for _ in v], [_[1] for _ in v])
        plt.show()
