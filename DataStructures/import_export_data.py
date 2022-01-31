import pandas as pd


# Import data from a CSV file
df = pd.read_csv('../data/scientists.csv')
# Select names column
names = df['Name']
# Export data in serialized or pickled format
# For a DataSeries
names.to_pickle('../export/names.pickle')
# For a DataFrame
df.to_pickle('../export/scientists.pickle')

# Import DataSeries from serialized or pickled format
names_series = pd.read_pickle('../export/names.pickle')
print(names_series)

# Import DataFrame from serialized or pickled format
scientists_df = pd.read_pickle('../export/scientists.pickle')
print(scientists_df.info())

# Export as CSV
scientists_df.to_csv('../export/scientists_pickle_csv.csv')
# Export as CSV without the row index
scientists_df.to_csv('../export/scientists_pickle_csv.csv', index=False)
# Export as Excel using xlwt package
scientists_df.to_excel('../export/scientists.xlsx', sheet_name='Scientists')
