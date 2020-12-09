import pandas as pd
from statsmodels.stats.anova import AnovaRM
from xarray.plot import plot

df = pd.read_csv('C:/Users/sarina/Desktop/analyze.csv')
aovrm = AnovaRM(df, 'Fluency', 'ID', within=['feedback'])
res = aovrm.fit()
df1 = pd.read_csv('C:/Users/sarina/Desktop/analyze.csv')
aovrm1 = AnovaRM(df, 'IOC', 'ID', within=['feedback'])
res1 = aovrm1.fit()
df2 = pd.read_csv('C:/Users/sarina/Desktop/analyze.csv')
aovrm2 = AnovaRM(df, 'Turn', 'ID', within=['feedback'])
res2 = aovrm2.fit()


print(res)
print(res1)
print(res2)
