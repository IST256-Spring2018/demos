import pandas as pd
import matplotlib.pyplot as plt

sh = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/master/superhero/superhero-movie-dataset-1978-2012.csv')


# no columns? no sweat!
sh.columns = [ 'year', 'title', 'comic', 'imdb', 'rt', 'composite', 'opening_weeked_bo', 'avg_ticket_price', 'opening_weekend_attend', 'us_pop_that_year']
print(sh.head())


## Who has more movies? DC or Marvel?
print(sh['comic'].value_counts())


## let's see that as a percentage of the total
print(sh['comic'].value_counts(normalize=True))


# ## what are the ratios in the last 10 years of data ?
filted_df = sh[ sh['year'] >2002]['comic'].value_counts(normalize=True)
# print(filted_df)

# # what about the first 10 years of data? 1978 - 1987?
print(sh[ sh['year'] < 1988]['comic'].value_counts(normalize=True))


# sh.head()

## skip nulls in analysis
sh2 = sh.dropna()

# # feature engineering
sh2 = sh2.assign(pct_of_pop=sh2['opening_weekend_attend'] /sh2['us_pop_that_year'])
print(sh2.head())

# # Marvel comics with highest opening_weeked_bo
#print(sh2[ sh2['comic'] == 'Marvel' ].sort_values('opening_weeked_bo').tail())

# Plotting!
sample_plot = sh.plot.bar(x ='year', y ='opening_weekend_attend', title="Some Chart" )
plt.show()