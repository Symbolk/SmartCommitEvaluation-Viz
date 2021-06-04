import os
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
import config

sns.set_theme(style='darkgrid')

path = os.path.join(config.usage_data_path, 'usage_week_user.csv')

df = pd.read_csv(path)

f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)

g1 = sns.lineplot(x='week', y='total_usage', ci="sd", data=df, ax=ax1)
g2 = sns.lineplot(x='week', y='total_generated_groups', ci="sd", data=df, ax=ax2)
g3 = sns.lineplot(x='week', y='total_manual_groups', ci="sd", data=df, ax=ax3)

# g = sns.relplot(x='week', y='total_usage', kind='line', ci='sd', data=df, ax = ax1)

ax1.set_ylabel('Usage')
ax1.set_xlabel('')
ax1.set_title('Usage Curve')

ax2.set_ylabel('Groups Num')
ax2.set_title('Generated Groups')
ax2.set_xlabel('')

# ax3.legend().set_visible(False)
ax3.set_ylabel('Groups Num')
ax3.set_title('Submitted Commits')
ax3.set_xlabel('Week')

plt.xlabel("Week")
plt.savefig(path.replace('.csv', '.pdf'), dpi=300, bbox_inches='tight')

plt.show()
