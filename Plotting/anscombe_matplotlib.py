import pandas as pd
import matplotlib.pyplot as plt

# Load data into a DataFrame and get an overview
df = pd.read_csv('../data/anscombe.csv')
print(df.info())
print(df.head())

# Separate anscombe dataset into groups
dataset_1 = df[df['dataset'] == 'I']
dataset_2 = df[df['dataset'] == 'II']
dataset_3 = df[df['dataset'] == 'III']
dataset_4 = df[df['dataset'] == 'IV']


# Create a matplotlib figure and 2x2 subplot grid
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

# Plot each group of data into its subplot
ax1.plot(dataset_1['x'], dataset_1['y'], 'o')
ax2.plot(dataset_2['x'], dataset_2['y'], 'o')
ax3.plot(dataset_3['x'], dataset_3['y'], 'o')
ax4.plot(dataset_4['x'], dataset_4['y'], 'o')

# Add title to each subplot
for i, ax in enumerate([ax1, ax2, ax3, ax4]):
    ax.set_title(f'Dataset {i + 1}')
    
# Title for figure
fig.suptitle("Anscombe Dataset Visualisation with Matplotlib")
# Reduce whitespace around the subplots
fig.tight_layout()
plt.show()

# Mean and standard deviation of the groups are same
# The differences in the dataset are seen only after visualisation.
df.groupby(['dataset']).mean()
df.groupby(['dataset']).std()

