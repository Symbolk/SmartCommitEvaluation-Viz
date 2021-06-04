import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import os
import csv
import config

csv_path = 'acc-lengths.csv'

if os.path.exists(csv_path):
    os.remove(csv_path)

if not os.path.isfile(csv_path):
    open_w = open(csv_path, "w")
    # header
    open_w.write('project,length,accuracy')
    open_w.close()

for r in config.repos:
    for s in config.lengths:
        raw_csv = config.root_path + 'SmartCommit/' + r + '_' + str(s) + '.csv'
        if not os.path.exists(raw_csv):
            print("%s does not exist!" % raw_csv)
        else:
            lines = []
            with open(raw_csv, 'r') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    line = [r, str(s), row['accuracy']]
                    lines.append(line)

            with open(csv_path, 'a') as open_a:
                for line in lines:
                    open_a.write('\n' + ','.join(line))

sns.set(style="whitegrid", font_scale=1.8)
df = pd.read_csv(csv_path)
g = sns.boxplot(x="project", y="accuracy", hue="length", data=df, palette="Set3")
plt.ylim(0, 100)
plt.yticks([0, 25, 50, 75, 100])
# plt.xlabel("Project")
# plt.ylabel("Accuracy (%)")
plt.xlabel("")
plt.ylabel("")
plt.setp(g.get_xticklabels(), rotation=45)
plt.legend(loc='lower center')
plt.legend(fontsize='x-small', title_fontsize='10')

plt.title("")
plt.savefig('rq1-length.pdf', dpi=300, bbox_inches='tight')
plt.show()
