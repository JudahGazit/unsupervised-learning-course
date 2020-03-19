import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from sklearn import manifold
from sklearn.cluster import DBSCAN
from sklearn.mixture import GaussianMixture

from python_code.learning.clustering.ICluster import ICluster
import numpy as np


class MDSClustering(ICluster):
    def __init__(self, dimensions=2, metric=True, clusters=2, **kwargs):
        self.graph_to_points = manifold.MDS(dimensions, metric=metric, dissimilarity='precomputed', **kwargs)
        # self.graph_to_points = manifold.TSNE()
        self.cluster_engine = GaussianMixture(clusters)

    def cluster(self, graph: nx.Graph, df=None, draw_results=True):
        nodes_list = sorted(list(graph.nodes()))
        adj_matrix = self.get_adj_matrix(graph, nodes_list)
        transformed = self.transform(adj_matrix)
        partition = self.partition_transformed(transformed)
        partition = pd.DataFrame(zip(nodes_list, transformed, partition), columns=['title', 'xy', 'community'])
        if df is not None:
            partition_with_win = partition.merge(df[['title', 'win']], on=['title'])
            self.draw_oscar_winners(partition_with_win)
        if draw_results:
            self.draw_partitions(partition)
        return partition

    def convert_weight_to_distance(self, w):
        if w > 0:
            return 1 / w
        return 0.0

    def get_adj_matrix(self, graph, nodes_list):
        adj_matrix = nx.adj_matrix(graph, nodes_list).toarray()
        fv = np.vectorize(self.convert_weight_to_distance)
        adj_matrix = fv(adj_matrix)
        return adj_matrix

    def partition_transformed(self, transformed):
        partition = self.cluster_engine.fit_predict(transformed)
        return partition

    def transform(self, adj_matrix):
        transformed = self.graph_to_points.fit_transform(adj_matrix)
        return transformed

    def draw_transformed(self, transformed):
        plt.scatter([_[0] for _ in transformed], [_[1] for _ in transformed])
        plt.show()

    def draw_oscar_winners(self, partition):
        partition.win = partition.win.apply(lambda v: 1 if v > 0 else 0)
        win_grouped = partition.groupby(['win'])
        win_grouped.xy = win_grouped.xy.apply(list)
        for v in win_grouped.xy.values:
            plt.scatter([_[0] for _ in v], [_[1] for _ in v])
        plt.show()

    def draw_partitions(self, partition):
        partition_grouped = partition.groupby(['community'])
        partition_grouped.xy = partition_grouped.xy.apply(list)
        for v in partition_grouped.xy.values:
            plt.scatter([_[0] for _ in v], [_[1] for _ in v])
        plt.show()
