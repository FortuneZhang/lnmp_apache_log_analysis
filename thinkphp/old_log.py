# coding=utf8

import os

#log_path = '/home/fz/project/work/miaopu-cn/Application/Runtime/Logs/Home'
log_path = '/data/wwwroot/www.miaoyoutong.com/Application/Runtime/Logs/Home'

time_limit_files = []
for dirpath, dirnames, filenames in os.walk(log_path):
    for filename in filenames:
        if ('log' in filename):
            log_file = dirpath + '/' + filename
            time = os.path.getctime(log_file)
            if (time > 1512057600):
                time_limit_files.append((log_file, time))

time_limit_files = sorted(time_limit_files, key= lambda x: x[1])

for log_file in time_limit_files:
    log_file = log_file[0]
    with open(log_file) as f:
        for line in f.readlines():
            line = line.lower()
            if "53520" in line and 'rft_member' in line and (('update' in line or 'insert' in line) and 'select' not in line):
                print(log_file + '->' + line)
