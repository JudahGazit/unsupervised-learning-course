import pandas as pd
from IPython.core.display import display

from python_code.learning.data_loader import load_data
from python_code.learning.graph.edges_logics.IEdgeLogic import IEdgeLogic
from python_code.learning.graph.edges_logics.cast_count import CastCount
from python_code.learning.graph.edges_logics.cast_priority_factor import CastPriorityFactor
from python_code.learning.graph.edges_logics.category import Category
from python_code.learning.graph.edges_logics.combine import Combine
from python_code.learning.graph.edges_logics.rating_diff import RatingDiff


def test_edge_logic(df: pd.DataFrame, edges_logics: [IEdgeLogic]):
    edge_by_rating_diff = RatingDiff().create_edges(df)
    for edges_logic in edges_logics:
        display(edges_logic.__class__.__name__)
        edges = edges_logic.create_edges(df)
        corr = edges.merge(edge_by_rating_diff, on=['src', 'dst'])
        corr = corr[['weight_x', 'weight_y']].corr()
        display(corr)


if __name__ == '__main__':
    df = load_data()
    edges_logics = [
        CastCount(),
        CastPriorityFactor(),
        Category(),
        Combine([CastPriorityFactor(), Category()]),
        Combine([CastCount(), Category()]),
    ]
    test_edge_logic(df, edges_logics)
