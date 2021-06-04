import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import os
import csv
import config

# aggregated data
csv_path = 'acc-methods.csv'

if os.path.exists(csv_path):
    os.remove(csv_path)

if not os.path.isfile(csv_path):
    open_w = open(csv_path, "w")
    # header
    open_w.write('project,method,length,accuracy')
    open_w.close()

# collect all desired samples into one file for viz
for r in config.repos:
    for s in config.lengths:
        for m in config.methods:
            raw_csv = config.root_path + m + '/' + r + '_' + str(s) + '.csv'
            if not os.path.exists(raw_csv):
                print("%s does not exist!" % raw_csv)
            else:
                lines = []
                with open(raw_csv, 'r') as f:
                    reader = csv.DictReader(f, delimiter=',')
                    for row in reader:
                        line = [r, m, str(s), row['accuracy']]
                        lines.append(line)

                with open(csv_path, 'a') as open_a:
                    for line in lines:
                        open_a.write('\n' + ','.join(line))

sns.set(style="whitegrid", font_scale=1.8)

df = pd.read_csv(csv_path)
g = sns.boxplot(x="project", y="accuracy", hue="method", data=df, palette="Set3")
# g.set_yticks(range(100, 25))

plt.ylim(0, 100)
plt.yticks([0, 25, 50, 75, 100])
# plt.figure(figsize=(20,8))
# plt.xlabel("Project")
plt.xlabel("")
plt.ylabel("Accuracy (%)")
plt.setp(g.get_xticklabels(), rotation=45)
plt.legend(loc='lower right')
plt.legend(fontsize='x-small', title_fontsize='10')

plt.title("")
plt.savefig('rq1-baselines.pdf', dpi=300, bbox_inches='tight')
plt.show()
