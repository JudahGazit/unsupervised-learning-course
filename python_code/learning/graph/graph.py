import networkx as nx


def create_graph(edges, component=None):
    if component is not None:
        edges = [(i, j, w) for (i, j, w) in edges.values if i in component]
    else:
        edges = edges.values
    graph = nx.Graph()
    graph.add_weighted_edges_from(edges)
    return graph
