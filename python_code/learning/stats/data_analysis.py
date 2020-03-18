import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from IPython.core.display import display


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
    display(df.corr())


def cast_stats(df: pd.DataFrame):
    ax = plt.subplot()
    df = df.explode('cast')
    df = df.groupby(['cast'], as_index=False).agg({'title': 'count'})
    df['title'].hist(bins=50)
    ax.set_title('cast members histogram')
    ax.set_xlabel('movies per cast member')
    plt.show()


def rating_histogram(df: pd.DataFrame):
    ax = plt.subplot()
    df['averageRating'].hist(bins=50)
    ax.set_title('Rating Histogram')
    ax.set_xlabel('Rating')
    plt.show()


def rating_histogram_oscar_winners(df: pd.DataFrame):
    ax = plt.subplot()
    df[df.win > 0]['averageRating'].hist(bins=50)
    ax.set_title('Rating Histogram - oscar winners only')
    ax.set_xlabel('Rating')
    plt.show()


def cast_member_rating_variance(df):
    df = df.explode('cast')
    d = df.groupby(['cast'], as_index=False)[['cast', 'averageRating']].agg(['min', 'max', 'mean', 'std', 'count'])
    d['diff'] = d['averageRating']['max'] - d['averageRating']['min']
    d[d['averageRating']['count'] > 1]['diff'].hist()
    plt.title('maximal diff between cast member\'s movies histogram')
    plt.xlabel('maximal diff between movie rating')
    plt.show()


def analyze(df, graph):
    graph_out_degree_histogram(graph)
    graph_weights_histogram(graph)
    corrolation_between_raiting_and_oscars(df)
    cast_stats(df)
    rating_histogram(df)
    rating_histogram_oscar_winners(df)
    cast_member_rating_variance(df)
