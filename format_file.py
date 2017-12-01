import time, re, json

log_re = '(?P<ip>[.:0-9a-fA-F]+) - - \[(?P<time>.*?)\] "(?P<method>[POST|GET]*?) (?P<uri>.*?) HTTP/1.\d" (?P<status_code>\d+) \d+ "(?P<referral>.*?)" "(?P<agent>.*?)"'
search = re.compile(log_re).search


def search_line_then_format(line):
    x = search(line)

    if x is None:
        return None

    return {
        'user_ip': x.group('ip'),
        'uri': x.group('uri'),
        'time': x.group('time'),
        'status_code': x.group('status_code'),
        'referral': x.group('referral'),
        'agent': x.group('agent'),
        'method': x.group('method'),
        'timestamp': int(time.mktime(time.strptime(x.group('time').replace(' +0800', ''), '%d/%b/%Y:%H:%M:%S')))
    }


def write_lines_to_file(lines, analysis_middle_result_file_name):
    with open(analysis_middle_result_file_name, 'a') as write_result:
        [write_result.write(json.dumps(x) + '\n') for x in lines]


def format(file_name, analysis_middle_result_file_name):
    with open(file_name, 'r') as f:
        results = []
        for line in f.readlines():
            result = search_line_then_format(line)

            if (result):
                results.append(result)

            if (len(results) >= 10):
                write_lines_to_file(results, analysis_middle_result_file_name)
                results = []
        write_lines_to_file(results, analysis_middle_result_file_name)
