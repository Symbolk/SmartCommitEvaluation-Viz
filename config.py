import os
from pathlib import Path

repos = ['netty', 'nomulus', 'glide', 'storm', 'realm-java',
         'deeplearning4j', 'elasticsearch', 'rocketmq', 'cassandra', 'antlr4']

methods = ['All', 'File', 'DefUse', 'SmartCommit']

lengths = [2, 3, 5]

# root dir of raw data
root_path = str(Path.home()) + '/smartcommit/viz/'
# root_path = str(Path.home()) + '/coding/data/viz/'

# path of the field study usage data
usage_data_path = os.path.dirname(os.path.realpath(__file__)) + "/cached/field_study_data"
