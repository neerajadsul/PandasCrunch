import pandas as pd


# Read CSV file into a DataFrame
scientists = pd.read_csv('../data/scientists.csv')
scientists.info
# Get Age column from the DataFrame
ages = scientists['Age']
# Descriptive statistics on Age
print(ages.describe())
# Vectorized selection 
print(ages > ages.mean())
# Vectorized selection and indexing
print(ages.loc[ages > ages.mean()])
# Vectorized selection and indexing on the DataFrame
print(scientists.loc[ages > ages.mean()])
# Vectorized math operations, element by element
print(ages + 100)
# Element by element addition, for missing values addition is NaN
ages + pd.Series([100,10])
# Sort by index
rev_ages = ages.sort_index(ascending=False)
# Indices are aligned before addition
print(ages + rev_ages)

