# coding = utf8
import json, time, sys, getopt, os

if __name__ == '__main__':
    shortargs = 'hi:o'
    longargs = ['filename=', 'content=', 'output=']
    opts, args = getopt.getopt(sys.argv[1:], shortargs, longargs)

    filename_contain = ''
    line_content_contain = ''
    output_file = 'log_find.txt'
    for op, value in opts:
        if op == "--filename":
            filename_contain = value
        elif op == "--content":
            line_content_contain = value
            line_content_contain = line_content_contain.split(',')
        elif op == "--output":
            output_file = value
        elif op == "-h":
            print('python main.py --filename 2018-03-03 --content 88,xx,yy')
            sys.exit()

    all_need_read_file_log_list = []
    for root, dirs, files in os.walk('./'):
        for file in files:
            if os.path.splitext(file)[1] == '.log':
                if filename_contain:
                    if filename_contain in file:
                        all_need_read_file_log_list.append(os.path.join(root, file))
                else:
                    all_need_read_file_log_list.append(os.path.join(root, file))

    for file in all_need_read_file_log_list:
        print(file)
        with open(file) as f:
            line_number = 0
            for line in f.readlines():
                line_number += 1

                is_in_line = True
                for line_c in line_content_contain:
                    is_in_line = is_in_line and line_c in line
                if is_in_line and output_file:
                    _line = str(line_number) + '---' + line
                    print(_line)
                    with open(output_file, 'a+') as write_file:
                        write_file.write(_line)
