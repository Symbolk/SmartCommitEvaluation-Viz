import os
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
import config

sns.set_theme(style='darkgrid')
sns.set(font_scale=2.0)

path = os.path.join(config.usage_data_path, 'usage_week.csv')

df = pd.read_csv(path)

# f, ax1 = plt.subplots()
g = sns.lineplot(x='week', y='total_users', data=df)


# g.fig.set_figwidth(6.8)
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
plt.ylabel("#Users")
# plt.title("Usage Curve")
plt.savefig(path.replace('usage_week.csv', 'users_week.pdf'), dpi=300, bbox_inches='tight')

plt.show()
