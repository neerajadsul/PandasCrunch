import pandas as pd


# Create a series with data
s = pd.Series(['LED', '660nm'])
# Create series supplied with an index 
s = pd.Series(['Red', '660nm'], index=['color','wavelength'])

# Typical way of creating a DataFrame is using dictionary
leds = {
    'color': ['Red', 'Green', 'Blue', 'NIR'],
    'wavelength_nm': ['660','532','440','750'],
    'mfg': ['osram', 'kingbright', 'kingbright', 'marektech']
    }

df = pd.DataFrame(leds)
print(df.head())

# DataFrame from a dict supplied with an index
df = pd.DataFrame(
    data = leds,
    index = leds['color']
    )
print(df.head())
# Get a row of the DataFrame which is a Series
green_row = df.loc['Green']
print(green_row)
# Some attributes of the Series
print(green_row.index)
print(green_row.values)
# Transpose a series
print(green_row.T)
