# coding = utf8
import json
import time
import format_file

analysis_middle_result_file_name = str(time.time()) + '.txt'

if __name__ == '__main__':
    format_file.format('www.miaoyoutong.com-access_log_2017_10_16_100000.log', analysis_middle_result_file_name)
    ips = {}

    with open(analysis_middle_result_file_name, 'r') as f:
        for line in f.readlines():
            line = json.loads(line)
            print(line)
            ip = line['user_ip']
            if ip in ips:
                ips[ip] += 1
            else:
                ips[ip] = 1

    print(ips)
