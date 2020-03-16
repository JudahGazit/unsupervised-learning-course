def test(df, partition, col='averageRating'):
    df = df.merge(partition, on=['title'])

title_and_community = pd.DataFrame(partition.items(), columns=['title', 'community'])\
                        .merge(stats[['community', 'g']], on=['community'])\
                        .merge(df, on=['title'])
title_and_community.win = title_and_community.win.apply(lambda v: v if v > 1 else 0)
summ = rp.summary_cont(title_and_community.groupby(['g'])[col])
display(summ)
g0 = title_and_community[title_and_community.g == 0].sample(n=100)
g0.reset_index(inplace=True)
g1 = title_and_community[title_and_community.g == 1].sample(n=100)
g1.reset_index(inplace=True)

levene_homogenity = scipy.stats.levene(g0[col], g1[col])
display(levene_homogenity)
diff = g1[col] - g0[col]
scipy.stats.probplot(diff, plot= plt)
plt.title('Raiting P-P Plot')
plt.show()
diff.plot(kind= "hist", title= "Raiting Residuals", bins=30)
plt.show()
display('Shapiro on diff:', scipy.stats.shapiro(diff))
display(scipy.stats.ttest_ind(g0[col], g1[col], equal_var=False))