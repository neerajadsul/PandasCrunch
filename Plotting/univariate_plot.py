# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
tips = pd.read_csv('../data/tips.csv')
tips.head()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.hist(tips['total_bill'], bins=10)
ax1.set_title('Histogram of total bill amount')
ax1.set_xlabel('Frquency')
ax1.set_ylabel('Total Bill')
plt.show()
