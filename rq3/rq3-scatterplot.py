import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import os
import csv

# process the raw data
import config

csv_path = 'time.csv'

if os.path.exists(csv_path):
    os.remove(csv_path)

if not os.path.isfile(csv_path):
    open_w = open(csv_path, "w")
    # header
    open_w.write('repo,length,#diff_hunks,run_time(ms),#LOC')
    open_w.close()

repos = ['netty', 'nomulus', 'rocketmq', 'realm-java', 'glide', 'storm'
    , 'elasticsearch', 'error-prone']

lengths = [2, 3, 5]
for r in repos:
    for s in lengths:
        raw_csv = config.root_path + 'SmartCommit/' + r + '_' + str(s) + '.csv'
        if not os.path.exists(raw_csv):
            print("%s does not exist!" % raw_csv)
        else:
            lines = []
            with open(raw_csv, 'r') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    line = [r, str(s), row['#diff_hunks'], row['runtime'], row['#LOC']]
                    lines.append(line)

            with open(csv_path, 'a') as open_a:
                for line in lines:
                    open_a.write('\n' + ','.join(line))

df = pd.read_csv(csv_path)
sns.set(style="whitegrid", font_scale=1)

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

# sns.boxplot(x='#diff_hunks', y='run_time(ms)', hue='size', data=df, palette='deep', ax=ax1)
sns.scatterplot(x='#diff_hunks', y='run_time(ms)', hue='length', style='length', data=df, palette='deep', ax=ax1)
sns.scatterplot(x='#LOC', y='run_time(ms)', hue='length', style='length', data=df, palette='deep', ax=ax2)
# g1._legend.remove()
# g2._legend.remove()

ax1.set_xlim(0, 500)
ax1.set_ylim(0, 10000)
ax1.set_xlabel('Number of Diff Hunks')
ax1.set_ylabel('Run Time (ms)')

ax2.set_xlim(0, 10000)
ax2.set_ylim(0, 10000)
ax2.set_xlabel('Number of Changed Lines')
# ax2.set_ylabel('Run Time in Milliseconds')

plt.title("")
# plt.legend()
plt.tight_layout()
plt.savefig('rq3.pdf', dpi=300)
plt.show()
