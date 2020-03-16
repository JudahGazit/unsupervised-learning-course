from IPython.core.display import display

from python_code.learning.data_loader import load_data
from python_code.learning.graph.edges_logics.cast_priority_factor import CastPriorityFactor
from python_code.learning.graph.edges_logics.category import Category
from python_code.learning.graph.edges_logics.combine import Combine
from python_code.learning.graph.graph import create_graph
from python_code.learning.louvain import Louvain
from python_code.learning.stats.cluster_stats import *


def get_graph(df):
    edges_logic = Combine([CastPriorityFactor(), Category()])
    edges = edges_logic.create_edges(df)
    graph = create_graph(edges)
    return graph


def stats(df, partition):
    stats = community_stats(df, partition)
    stats = stats_threshold(stats)
    stats = precision_recall(stats)
    return stats


def cluster(graph):
    louvain = Louvain()
    partition = louvain.cluster(graph)
    return partition


def main():
    df = load_data()
    graph = get_graph(df)
    partition = cluster(graph)
    display(stats(df, partition))


if __name__ == "__main__":
    main()
