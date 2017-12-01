# coding = utf8
import json
import time
import format_file
import analysis_file

analysis_middle_result_file_name = str(time.time()) + '.txt'

if __name__ == '__main__':
    format_file.format('www.miaoyoutong.com-access_log_2017_10_16_100000.log', analysis_middle_result_file_name)
    result = analysis_file.analysis(analysis_middle_result_file_name)
    for ip,count in result.items():
        print(ip + '->' + str(count))


