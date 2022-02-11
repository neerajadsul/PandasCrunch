# coding: utf-8
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


tips = pd.read_csv('../data/tips.csv')

sns.set_style('whitegrid')

ax = sns.kdeplot(data=tips, x='total_bill', y='tip', fill=True)
ax.set(title='KDE (Kernal Density Estimation) Plot')
plt.tight_layout()
plt.show()

sns.set_style('darkgrid')
sns.jointplot(data=tips, x='total_bill', y='tip',kind='kde', fill=True)
ax.set(title='JointPlot')
plt.tight_layout()
plt.grid(True)
plt.show()

sns.set_style('dark')
sns.barplot(data=tips, x='time', y='tip')
ax.set(title='BarPlot')
plt.show()

sns.boxplot(data=tips, x='time', y='tip')
ax.set(title='BoxPlot')
plt.show()

sns.violinplot(data=tips, x='time', y='tip')
ax.set(title='ViolinPlot')
plt.show()

sns.pairplot(tips)
plt.show()


pair_grid = sns.PairGrid(tips)
pair_grid = pair_grid.map_upper(sns.regplot)
pair_grid = pair_grid.map_lower(sns.kdeplot)
pair_grid = pair_grid.map_diag(sns.histplot)
plt.show()
