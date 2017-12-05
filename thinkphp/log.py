# coding=utf8

import os

log_path = '/wwwroot/Application/Runtime/Logs/Home'


def write_result_to_file(log_file, line):
    with open('find_result.txt', 'a') as f:
        f.write(log_file + '->' + line + '\n')


for dirpath, dirnames, filenames in os.walk(log_path):
    filecount = len(filenames)
    for filename in filenames:
        print('#', end='')
        if ('log' in filename):
            log_file = dirpath + '/' + filename
            with open(log_file) as f:
                for line in f.readlines():
                    if ("40503" in line):
                        write_result_to_file(log_file, line)
