import pandas as pd


def community_stats(df, communities):
    df = df.copy()
    df = df.merge(communities, on=['title'])
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


def add_threshold(stats, threshold=7.9):
    stats = stats.copy()
    stats['g'] = stats.max_raiting.apply(lambda v: 1 if v >= threshold else 0)
    return stats


def stats_threshold(stats, threshold=7.9):
    stats = add_threshold(stats, threshold)
    stats_g = stats.groupby(['g']).agg({'title': 'sum', 'win_movies': 'sum', 'win_and_nominated_movies': 'sum',
                                        'max_raiting': 'max', 'min_raiting': 'min', 'averageRating': 'mean'})
    return stats_g


def precision_recall(stats):
    stats = stats.copy()
    total_win = stats.win_movies.sum()
    total_win_and_nom = stats.win_and_nominated_movies.sum()
    stats['win_precision'] = 100 * stats.win_movies / stats.title
    stats['win_recall'] = 100 * stats.win_movies / total_win
    stats['win_nom_precision'] = 100 * stats.win_and_nominated_movies / stats.title
    stats['win_nom_recall'] = 100 * stats.win_and_nominated_movies / total_win_and_nom
    return stats


def find_best_cut_by_max_rating(stats):
    s = stats[['title', 'win_movies', 'max_raiting']].sort_values('max_raiting', ascending=False)
    s.reset_index(inplace=True)
    s['rolling_title'] = pd.Series([s.title[:r + 1].sum() for r in range(len(s.title))])
    s['rolling_win'] = pd.Series([s.win_movies[:r + 1].sum() for r in range(len(s.win_movies))])
    s['rolling_precision'] = s.rolling_win / s.rolling_title
    total_win = s.win_movies.sum()
    s['rolling_recall'] = s.rolling_win / total_win
    best_rating_cut = s[(s.rolling_recall >= 0.5)].sort_values(['rolling_precision'], ascending=False).head(1)
    return best_rating_cut
