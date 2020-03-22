import matplotlib.pyplot as plt
import researchpy as rp
import scipy
from IPython.core.display import display

from python_code.learning.stats.cluster_stats import community_stats, add_threshold


def split_to_groups(df):
    g0 = df[df.g == 0].sample(n=100, random_state=40)
    g0.reset_index(inplace=True)
    g1 = df[df.g == 1].sample(n=100, random_state=40)
    g1.reset_index(inplace=True)
    return g0, g1


def run_ttest(col, g0, g1, w_test=True):
    ttest = scipy.stats.ttest_ind(g0[col], g1[col], equal_var=not w_test)
    display(ttest)


def run_shapiro(diff):
    scipy.stats.probplot(diff, plot=plt)
    plt.title('Raiting P-P Plot')
    plt.show()
    diff.plot(kind="hist", title="Raiting Residuals", bins=30)
    plt.show()
    display('Shapiro on diff:', scipy.stats.shapiro(diff))


def run_levene(col, g0, g1):
    levene_homogenity = scipy.stats.levene(g0[col], g1[col])
    display(levene_homogenity)
    return levene_homogenity


def summerize(col, df):
    summ = rp.summary_cont(df.groupby(['g'])[col])
    display(summ)


def test(df, partition, col='averageRating'):
    """
    Running Welch's t-test on the groups we created.
    We try to compare 2 samples from the groups.
    We summarize the the data, and then run 3 tests:
    1. levenve test - to see if the variance is equal between the cluster.
        if the answer in owr case is negative, we pass the param `equal_var=False` to the ttest to initiate Welch's test
    2. We test if the difference between the groups to be a normal distribution. First we do it visually,
        and afterward with Shapiro
    3. We run Welch's t-test after the assumptions have met.

    :param df:
    :param partition:
    :param col:
    """
    stats = community_stats(df, partition)
    stats = add_threshold(stats)
    df = df.merge(partition, on=['title']).merge(stats[['community', 'g']], on=['community'])
    g0, g1 = split_to_groups(df)

    summerize(col, df)
    levene_homogenity = run_levene(col, g0, g1)
    diff = g1[col] - g0[col]
    run_shapiro(diff)
    run_ttest(col, g0, g1, levene_homogenity.pvalue <= 0.05)
