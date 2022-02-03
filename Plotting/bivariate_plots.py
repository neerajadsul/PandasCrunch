# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
tips = pd.read_csv('../data/tips.csv')
fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.scatter(tips['total_bill'], tips['tip'])
ax1.set_title('Tip vs Total Bill')
ax1.set_xlabel('Total Bill')
ax1.set_ylabel('Tip')
ax2.boxplot(
    [tips[tips['sex'] == 'Female']['tip'],
    tips[tips['sex'] == 'Male']['tip'],
    labels=['Female', 'Male']]
    )
ax2.boxplot(
    [tips[tips['sex'] == 'Female']['tip'],
    tips[tips['sex'] == 'Male']['tip']],
    labels=['Female', 'Male']
    )
ax2.set_xlabel('Sex')
ax2.set_ylabel('Tip')
ax2.set_title('Tips by Sex')
plt.show()
