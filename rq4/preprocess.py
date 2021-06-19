import pandas as pd
import os
import datetime
import config

root = config.root_path


def prepare(path, header):
    if os.path.exists(path):
        os.remove(path)

    if not os.path.isfile(path):
        with open(path, 'w') as fw:
            fw.write(header)
            print("Results will be saved in: " + path)


def same_week(date1, date2):
    d1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
    return d1.isocalendar()[1] == d2.isocalendar()[1] and d1.year == d2.year


def count_controls(df):
    total = coarse = fine = 0
    no_change = 0
    for index, row in df.iterrows():
        total += 1
        if row['coarse_control'] > 0:
            coarse += 1
        if row['fine_moving'] > 0:
            fine += 1
        if row['coarse_control'] == 0 and row['fine_moving'] == 0:
            no_change += 1
    print('{},{},{},{}'.format(total, coarse, fine, no_change))


def agg_by_time(df):
    groups = df.groupby(['time'])

    path = 'usage_data/usage_time1.csv'
    prepare(path, 'time,total_usage,total_generated_groups,total_manual_groups')
    with open(path, 'a') as fa:
        for time, group in groups:
            line = []
            # if pd.Timestamp(time).dayofweek > 4:
            #     continue
            line.append(time)
            line.append(len(group))
            g = m = 0
            for i, row in group.iterrows():
                g += row['generated_groups']
                m += row['manual_groups']
            line.append(g)
            line.append(m)

            fa.write('\n' + ','.join([str(l) for l in line]))


def agg_by_time_user(df):
    groups = df.groupby(['time', 'userId'])
    path = 'usage_data/usage_time_user1.csv'
    prepare(path, 'time,userId,total_usage,total_generated_groups,total_manual_groups')
    with open(path, 'a') as fa:
        for group_name, group in groups:
            line = []
            # if pd.Timestamp(group_name[0]).dayofweek > 4:
            #     continue
            line.append(group_name[0])
            line.append(group_name[1])
            line.append(len(group))
            g = m = 0
            for i, row in group.iterrows():
                g += row['generated_groups']
                m += row['manual_groups']
            line.append(g)
            line.append(m)

            fa.write('\n' + ','.join([str(l) for l in line]))


def hue_groups(df):
    groups = df.groupby(['time', 'userId'])
    path = 'usage_data/groups_time_user.csv'
    prepare(path, 'time,userId,groups,label')
    with open(path, 'a') as fa:
        for group_name, group in groups:
            line = []
            # if pd.Timestamp(group_name[0]).dayofweek > 4:
            #     continue
            line.append(group_name[0])
            line.append(group_name[1])
            g = m = 0
            for i, row in group.iterrows():
                g += row['generated_groups']
                m += row['manual_groups']
            fa.write('\n' + ','.join([str(l) for l in line]) + ',' + str(g) + ',generated')
            fa.write('\n' + ','.join([str(l) for l in line]) + ',' + str(m) + ',manual')


def agg_by_week(df):
    groups = df.groupby(['week'])
    path = os.path.join(root, 'usage_data/usage_week.csv')
    prepare(path, 'week,total_users,total_usage,total_generated_groups,total_manual_groups')
    all_users = set()
    with open(path, 'a') as fa:
        for group_name, group in groups:
            user_set = set()
            line = []
            # if pd.Timestamp(group_name[0]).dayofweek > 4:
            #     continue
            line.append(group_name)
            g = m = 0
            for i, row in group.iterrows():
                user_set.add(row['userId'])
                all_users.add(row['userId'])
                g += row['generated_groups']
                m += row['manual_groups']

            line.append(len(user_set))
            line.append(len(group))
            line.append(g)
            line.append(m)

            fa.write('\n' + ','.join([str(l) for l in line]))
    print(len(all_users))


def add_week_column(df):
    path = 'usage_data/out.csv'
    week = 0
    last_time = ''
    prepare(path,
            'time,year,month,week,day,userId,files_num,changed_loc,generated_groups,manual_groups,coarse_control,fine_moving')
    with open(path, 'a') as fa:
        for index, row in df.iterrows():
            line = []
            line.append(row['time'])
            line.append(row['year'])
            line.append(str(row['month']))
            if last_time == '':
                last_time = row['time']
                line.append(week)
            else:
                if not same_week(last_time, row['time']):
                    week += 1
                line.append(week)
                last_time = row['time']
            line.append(str(row['day']))
            line.append(row['userId'])
            line.append(row['files_num'])
            line.append(row['changed_loc'])
            line.append(row['generated_groups'])
            line.append(row['manual_groups'])
            line.append(row['coarse_control'])
            line.append(row['fine_moving'])
            fa.write('\n' + ','.join([str(l) for l in line]))


def agg_by_week_user(df):
    groups = df.groupby(['week', 'userId'])
    path = 'usage_data/usage_week_user.csv'
    prepare(path, 'week,userId,total_usage,total_generated_groups,total_manual_groups')
    with open(path, 'a') as fa:
        for group_name, group in groups:
            line = []
            line.append(group_name[0])
            line.append(group_name[1])
            line.append(len(group))
            g = m = 0
            for i, row in group.iterrows():
                g += row['generated_groups']
                m += row['manual_groups']
            line.append(g)
            line.append(m)

            fa.write('\n' + ','.join([str(l) for l in line]))


def hue_groups_week(df):
    groups = df.groupby(['week', 'userId'])
    path = os.path.join(root, 'usage_data/groups_week_user.csv')
    prepare(path, 'week,userId,groups,label')
    with open(path, 'a') as fa:
        for group_name, group in groups:
            line = []
            line.append(int(group_name[0]))
            line.append(int(group_name[1]))
            g = m = 0
            for i, row in group.iterrows():
                g += int(row['generated_groups'])
                m += int(row['manual_groups'])
            fa.write('\n' + ','.join([str(l) for l in line]) + ',' + str(g) + ',generated')
            fa.write('\n' + ','.join([str(l) for l in line]) + ',' + str(m) + ',manual')


# compute #weeks each user used the tool
def compute_used_week(df):
    groups = df.groupby(['userId'])
    path = os.path.join(root, 'user_week_uses.csv')
    prepare(path, 'userId,weeks,#weeks,#total_uses')
    with open(path, 'a') as fa:
        for group_name, group in groups:
            line = []
            line.append(group_name)
            weeks = set()
            for i, row in group.iterrows():
                weeks.add(int(row['week']))

            line.append('&'.join(str(w) for w in weeks))
            line.append(len(weeks))
            line.append(len(group))

            fa.write('\n' + ','.join([str(l) for l in line]))


if __name__ == '__main__':
    # agg_by_time(df)
    # count_controls(df)
    # add_week_column(pd.read_csv('statistics.csv'))

    # agg_by_week_user(pd.read_csv('20200518-20210123.csv'))
    # hue_groups_week(pd.read_csv(os.path.join(root, '20200518-20210123.csv')))
    # agg_by_week(pd.read_csv(os.path.join(root, '20200518-20210123.csv')))
    compute_used_week(pd.read_csv(os.path.join(config.usage_data_path, '20200518-20210123.csv')))
