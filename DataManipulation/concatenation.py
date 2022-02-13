# coding: utf-8
import pandas as pd


df1 = pd.read_csv('../data/concat_1.csv')
df2 = pd.read_csv('../data/concat_2.csv')
df3 = pd.read_csv('../data/concat_3.csv')

row_combined = pd.concat([df1, df2, df3])
print(row_combined)
print(row_combined.info())

new_df = pd.DataFrame([['n1','n2','n3','n4']], columns=['A','B','C','D'])

print(pd.concat([df1, new_df]))
# Rests the row indices
pd.concat([df1, df2], ignore_index=True)

# Combine the columns
print(pd.concat([df1,df2,df3], axis=1))

# Add a new column
df1['E'] = ['z1', 'z2', 'z3', 'z4']
df1['F'] = list(range(4))
print(df1)

# Combine columns and reset indices
print(pd.concat([df1,df2,df3], axis=1, ignore_index=True))

# Change column names
df2.columns = ['E','F','G','H']

# Combine columns shared between dataframes with 'inner'
pd.concat([df1, df2], join='inner')
# Default concatenation
pd.concat([df1, df2], join='outer')
