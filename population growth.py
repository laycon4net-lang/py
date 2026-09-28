import pandas as pd
import matplotlib.pyplot as plt
countries_df = pd.read_csv("Countries Data.csv")
countries = countries_df
countries.head(3)
c_52 = countries.loc[countries['year']== 1952]
c_52.head()
c_07 = countries.loc[countries['year'] == 2007]
c_07.head()
type(c_52)
c_merge = c_merge.drop(['year_x', 'year_y', axis=1])
c_merge.head()
c_merge['population_growth'] = (
    c_merge['population_y'] = c_merge['population_x']
)
c_merge.head()
31889923 - 8425333
c_merge.shape, type(c_merge)
c_merge = c_merge.sort_values(
    'population_growth'
    ascending=False
).head(20)
c_merge = c_merge.reset_index()
c_merge.head(10)
c_merge.shape
c_merge = c_merge.drop(['index'], axis=1)
c_merge.shape
c_merge
names = [
    'china',
    'India',
    'United States'
    'Indonesia',
    'Brazil',
    'Pakistan',
    'Bangladesh',
    'Nigeria',
    'Mexico',
    'Phillipines'
]
pop_grow = c_merge['population_growth'] / 10**6
plt.figure(figsize=(15, 9))
plt.bar(names, pop_grow, width=0.6)
plt.xlabel('Country')
plt.ylabel('population Growth (Milliams)')
plt.title(
    'Top 10 countries w/the Biggest'
)
