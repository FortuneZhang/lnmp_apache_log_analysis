# coding = utf8
import json
import time
import format_file
import analysis_file

analysis_middle_result_file_name = str(time.time()) + '.txt'

if __name__ == '__main__':
    format_file.format('www.miaoyoutong.com-access_log_2017_10_16_100000.log', analysis_middle_result_file_name)
    result = analysis_file.analysis(analysis_middle_result_file_name)

    result = sorted(result.items(), key=lambda d: d[1], reverse=True)
    for item in result:
        print(item[0] , str(item[1]),sep='->')


