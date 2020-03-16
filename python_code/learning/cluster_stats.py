def community_stats(df, communities):
    df = df.copy()
    df['community'] = df.title.apply(lambda title: communities.get(title))
    df['max_raiting'] = df.averageRating
    df['min_raiting'] = df.averageRating
    df['stdRating'] = df.averageRating
    df['movie'] = df.type.apply(lambda t: 1 if t == 'Movie' else 0)
    df['tv_show'] = df.type.apply(lambda t: 1 if t == 'TV Show' else 0)
    df['win_movies'] = df.win.apply(lambda c: 1 if c > 0 else 0)
    df['win_and_nominated_movies'] = df.win.apply(lambda c: 1 if c >= 0 else 0)
    df = df.groupby(['community'], as_index=False).agg({'title': 'count',
                                                        'averageRating': 'mean',
                                                        'stdRating': 'std',
                                                        'win': 'sum',
                                                        'win_movies': 'sum',
                                                        'win_and_nominated_movies': 'sum',
                                                        'max_raiting': 'max',
                                                        'min_raiting': 'min',
                                                        'movie': 'sum',
                                                        'tv_show': 'sum',
                                                        })
    df = df.sort_values(['title'], ascending=False)
    return df


def stats_threshold(stats, threshold=7.9):
    stats['g'] = stats.max_raiting.apply(lambda v: 1 if v >= threshold else 0)
    stats_g = stats.groupby(['g']).agg({'title': 'sum', 'win_movies': 'sum', 'win_and_nominated_movies': 'sum',
                                        'max_raiting': 'max', 'min_raiting': 'min', 'averageRating': 'mean'})
    return stats_g


def precision_recall(stats_g):
    stats_g = stats_g.copy()
    total_win = stats_g.win_movies.sum()
    total_win_and_nom = stats_g.win_and_nominated_movies.sum()
    stats_g['win_precision'] = 100 * stats_g.win_movies / stats_g.title
    stats_g['win_recall'] = 100 * stats_g.win_movies / total_win
    stats_g['win_nom_precision'] = 100 * stats_g.win_and_nominated_movies / stats_g.title
    stats_g['win_nom_recall'] = 100 * stats_g.win_and_nominated_movies / total_win_and_nom
    return stats_g
