import networkx as nx


def create_graph(edges, component=None):
    if component is not None:
        edges = [(i, j, w) for (i, j, w) in edges.values if i in component]
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    return G
