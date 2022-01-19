import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into a DataFrame
df = pd.read_csv('../data/gapminder.tsv', sep='\t')
# Get summary of the data
print(df.info)
# Grouping data by year and statistics on grouped life expectancy
grouped_mean = df.groupby('year')['lifeExp'].mean()
groupded_std = df.groupby('year')['lifeExp'].std()
# Grouping data in multiple groups and stats on groups for specific columns
multi_grouped_mean = df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean()
# Get unique datapoints for grouping
unique_datapoints = df.groupby(['year','continent'])[['lifeExp','gdpPercap']].nunique()
# Print as a table , flattened data
print(multi_grouped_mean.reset_index())
# Grouping, stats and simple plots with data
global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()

plt.subplot(1,3,1)
global_yearly_life_expectancy.plot()
plt.title('Yearly Global Life Expectancy')
plt.xlabel('Year')
plt.ylabel('Mean Life Expectancy in years')

plt.subplot(1,3,2)
df.groupby('continent')['lifeExp'].mean().plot()
plt.title('Yearly Continental Life Expectancy')
plt.xlabel('Continent')
plt.ylabel('Mean Life Expectancy in Years')

plt.subplot(1,3,3)
df.groupby('gdpPercap')['lifeExp'].mean().plot()
plt.title('Yearly Life Expectancy as per GDP PPP')
plt.xlabel('GDP PPP')
plt.ylabel('Mean Life Expectancy in Years')

plt.show()