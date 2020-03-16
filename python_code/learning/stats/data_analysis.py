import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


def graph_out_degree_histogram(graph: nx.Graph):
    degrees = nx.degree(graph)
    ax = plt.subplot()
    pd.DataFrame(dict(degrees).items(),
                 columns=['title', 'degree']).degree.hist(bins=50)
    ax.set_title('Node degree histogram')
    ax.set_xlabel('degree')
    plt.show()


def graph_weights_histogram(graph: nx.Graph):
    ax = plt.subplot()
    weights = []
    for src, dst in graph.edges:
        weight = graph.get_edge_data(src, dst)['weight']
        weights.append((src, dst, weight))
    pd.DataFrame(weights, columns=['src', 'dst', 'weight']).weight.hist(bins=50)
    ax.set_title('edge weight histogram')
    ax.set_xlabel('weight')
    plt.show()


def corrolation_between_raiting_and_oscars(df):
    df = df[['averageRating', 'win']]
    df.corr()
    display(df)


def analyze(df, graph):
    graph_out_degree_histogram(graph)
    graph_weights_histogram(graph)
    corrolation_between_raiting_and_oscars(df)
