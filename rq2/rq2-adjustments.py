from collections import defaultdict, OrderedDict

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import os
import csv
import config

# from scipy.stats import chi2

csv_path = 'ops.csv'

if os.path.exists(csv_path):
    os.remove(csv_path)

if not os.path.isfile(csv_path):
    open_w = open(csv_path, "w")
    # header
    # open_w.write('repo,size=2,size=3,size=5')
    open_w.write('repo,percent')
    open_w.close()

cnter = defaultdict(int)
cnter2 = defaultdict(float)
total = 0
for r in config.repos:
    cols = []  # 3 * 100

    for s in config.lengths:
        col = []
        raw_csv = config.root_path + 'SmartCommit/' + r + '_' + str(s) + '.csv'
        if not os.path.exists(raw_csv):
            print("%s does not exist!" % raw_csv)
        else:
            with open(raw_csv, 'r') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    # if int(row['#diff_hunks']) > 0:
                        # percent = round(float(row['#reassign']) / float(row['#diff_hunks']), 1)
                        # percent = (row['#reassign'])
                        # col.append(str(percent))
                        # cnter2[percent] += 1
                    # col.append(row['#reassign'])
                    cnter[int(row['#reassign'])] += 1
                    cnter2[int(row['#reorder'])] += 1
                    total += 1
        cols.append(col)
    # reverse and write

    rows = list(map(list, zip(*cols)))
    with open(csv_path, 'a') as open_a:
        for row in rows:
            # open_a.write('\n' + r + "," + ','.join(row))
            for p in row:
                open_a.write('\n' + r + "," + p)

print("reassign_frequency")
print("------")
print("{} : {} : {}".format("number", "times", "percentage"))
print("------")
for k, v in dict(sorted(cnter.items())).items():
    percent = int(v) * 100 / total
    print("{} : {} : {}".format(str(k), str(v), str(percent)))

print()
print("reorder_frequency")
print("------")
print("{} : {} : {}".format("number", "times", "percentage"))
print("------")

t = 0
for k, v in dict(sorted(cnter2.items())).items():
    percent = v * 100 / total
    t += percent
    print("{} : {} : {}".format(str(k), str(int(v)), str(percent)))