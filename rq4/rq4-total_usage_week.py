import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import os
import matplotlib.ticker as ticker

import config

sns.set_theme(style='darkgrid')

path = os.path.join(config.usage_data_path, 'usage_week.csv')

df = pd.read_csv(path)

# g.fig.set_figwidth(15)

f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)

g1 = sns.lineplot(x='week', y='total_usage', data=df, ax=ax1)
g2 = sns.lineplot(x='week', y='total_generated_groups', data=df, ax=ax2)
g3 = sns.lineplot(x='week', y='total_manual_groups', data=df, ax=ax3)

ax1.set_ylabel('Total Usage')
ax1.set_xlabel('')
ax1.set_title('Usage Curve')
ax1.set_ylim(bottom=0)

ax2.set_ylabel('Groups Num')
ax2.set_title('Generated Groups')
ax2.set_xlabel('')
ax2.set_ylim(bottom=0)

# ax3.legend().set_visible(False)
ax3.set_ylabel('Commits Num')
ax3.set_title('Submitted Commits')
ax3.set_xlabel('Week')
ax3.set_ylim(bottom=0)

plt.xlabel("Week")
plt.savefig(path.replace('.csv', '.pdf'), dpi=300, bbox_inches='tight')

plt.show()
