import pandas as pd

from python_code.learning.graph.edges_logics.IEdgeLogic import IEdgeLogic


class Combine(IEdgeLogic):
    def __init__(self, iedge_logics):
        """
        :param iedge_logics: list of IEdgeLogic
        """
        self.iedge_logics = iedge_logics

    def create_edges(self, df: pd.DataFrame):
        edges = self.iedge_logics[0].create_edges(df)
        for edge_logic in self.iedge_logics[1:]:
            edges = edges.merge(edge_logic.create_logic(df), on=['src', 'dst'], how='left')
            edges.weight_y = edges.weight_y.apply(lambda x: x + 1 if x > 0 else 1)
            edges['weight'] = edges.weight_x * edges.weight_y
            edges = edges[['src', 'dst', 'weight']]
        return edges
