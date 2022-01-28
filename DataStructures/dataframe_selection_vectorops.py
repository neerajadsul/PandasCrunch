import pandas as pd

# Read data and get an overview of it
df = pd.read_csv('../data/scientists.csv')
print(df.columns)
print(df.dtypes)

# Vectorized selection by a criteria
print(df['Age'] > df['Age'].mean())
print(df[df['Age'] > df['Age'].mean()])
first_half = df[:4]
second_half = df[4:]
# Element by element operation
print(first_half * 2)
