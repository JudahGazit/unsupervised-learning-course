from IPython.core.display import display
import pandas as pd

RESOLUTIONS = [0.1, 1, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100]


def hyper_opts(df, graph, cluster_engine, stats, args_list, result_filename='hyperopts2.csv'):
    stat = []
    for args in args_list:
        display(args)
        partition = cluster_engine(*args).cluster(graph)
        s = stats(df, partition)
        s['args'] = ', '.join(map(str, args))
        stat.append(s)
    pd.concat(stat).to_csv(result_filename)
