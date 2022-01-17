import pandas as pd

# Read a CSV file as a dataframe, data is separated by tab character
df = pd.read_csv('../data/gapminder.tsv', sep='\t')
# Show first five rows
print(df.head())
# Show number of rows, number of columns
print(df.shape)
# Show column headings
print(df.columns)
# Show datatypes of each column
print(df.dtypes)
# Shows summary of the DataFrame
print(df.info)
# Selects column with heading 'country'
country_df = df['country']
# Shows first five rows of the country column
print(country_df.head())
# Shows last five rows of the country column
print(country_df.tail())
# Shows summary of the country columns
print(country_df.info())

# Selects columns with specified labels
subset = df[['country', 'continent', 'year']]
print(subset.head())
print(subset.tail())
# Shows 3 entries from head
print(df.head(n=3))
# Shows 3 entries with given Index Label
# since it is a Label -1 doesn't work
print(df.loc[[1,3,15]])
# Shows last row
print(df.iloc[7:45:3,[0,3,1]])
# Slicing the rows and columns by indices
print(df.iloc[7:45:3,[0,3,-1]])
