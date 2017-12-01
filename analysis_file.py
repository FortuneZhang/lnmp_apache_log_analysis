import json


def analysis(middle_file_name):
    ips = {}

    with open(middle_file_name, 'r') as f:
        for line in f.readlines():
            line = json.loads(line)
            ip = line['user_ip']
            if ip in ips:
                ips[ip] += 1
            else:
                ips[ip] = 1

    return ips

