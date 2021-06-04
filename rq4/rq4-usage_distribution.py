import os
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
import config

sns.set_theme(style='darkgrid')
sns.set(font_scale=2.0)

path = os.path.join(config.usage_data_path, 'usage_week_user.csv')

df = pd.read_csv(path)

# f, ax1 = plt.subplots()
g = sns.relplot(x='week', y='total_usage', kind='line', data=df)
# g1 = sns.boxplot(x="week", y="total_usage", data=df, palette="Set3")


g.fig.set_figwidth(6.8)
print(plt.rcParams.get('figure.figsize'))

plt.xlim(left=1)
plt.xlim(right=36)
plt.ylim(bottom=0)
plt.ylim(top=25)
plt.xticks([1, 5, 10, 15, 20, 25, 30, 36])
# plt.xticks(rotation=-90)
# g.set_xticks(range(len(df), 5))
# g.set_xticklabels(range(len(df), 4))
# plt.xticks(np.arange(1, 150, 3))
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.xaxis.set_major_formatter(ticker.ScalarFormatter())

plt.xlabel("Week")
plt.ylabel("Usage/User")
# plt.title("Usage Curve")
plt.savefig(path.replace('csv', 'pdf'), dpi=300, bbox_inches='tight')

plt.show()
