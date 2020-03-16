from IPython.core.display import display

from python_code.learning.data_loader import load_data
from python_code.learning.graph.edges_logics.cast_priority_factor import CastPriorityFactor
from python_code.learning.graph.edges_logics.category import Category
from python_code.learning.graph.edges_logics.combine import Combine
from python_code.learning.graph.graph import create_graph

if __name__ == "__main__":
    df = load_data()
    edges_logic = Combine([CastPriorityFactor(), Category()])
    edges = edges_logic.create_edges(df)
    create_graph(edges)
    display(edges)
