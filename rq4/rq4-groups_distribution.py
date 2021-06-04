import os
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
import config

sns.set_theme(style='darkgrid')
sns.set(font_scale=2.0)

path = os.path.join(config.usage_data_path, 'groups_week_user.csv')

df = pd.read_csv(path)

f, ax1 = plt.subplots(figsize=(6.8,4.8))

g = sns.lineplot(x='week', y='groups', hue='label', ci="sd", data=df, ax=ax1)
# g1 = sns.boxplot(x='week', y='groups', hue='label', ax=ax1)

# plt.xlim(left=0)
# f.set_size_inches(6.4, 4.9)
# g.fig.set_figwidth(6.8)
# print(plt.rcParams.get('figure.figsize'))
plt.xlim(left=1)
plt.ylim(bottom=0)
plt.xlim(right=36)
plt.xticks([1, 5, 10, 15, 20, 25, 30, 36])

# g.set_xticks(range(len(df), 5))
# g.set_xticklabels(range(len(df), 4))
# plt.xticks(np.arange(1, 150, 3))
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(5))
# ax1.xaxis.set_major_formatter(ticker.ScalarFormatter())

plt.xlabel("Week")
plt.ylabel("#Groups/User")
# plt.title("Groups Curve")
plt.savefig(path.replace('csv', 'pdf'), dpi=300, bbox_inches='tight')

plt.show()
