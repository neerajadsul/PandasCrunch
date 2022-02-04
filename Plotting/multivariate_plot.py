import pandas as pd
import matplotlib.pyplot as plt


tips = pd.read_csv('../data/tips.csv')
tips['color_by_sex'] = tips['sex'].apply(lambda s: 'red' if s == 'Female' else 'blue')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.scatter(
    x=tips['total_bill'],
    y=tips['tip'],
    s=tips['size'] * 25,
    c=tips['color_by_sex'],
    alpha=0.5,
    )

ax1.set_title('Total Bill vs Tip coloured by Sex and sized by Party Size')
ax1.set_xlabel('Total Bill')
ax1.set_ylabel('Tip')
plt.show()
