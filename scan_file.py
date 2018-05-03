import sys
import os
import subprocess
from utils import api_dbs


def get_file_strings(file_name):
    """
    获取文件strings集合
    """
    cmd = 'strings %s' % file_name
    out = subprocess.check_output(cmd, shell=True).decode('utf-8')
    set_keywords = set(out.split())
    return list(set_keywords)


def find_private_apis(file_name):
    """
    搜索指定文件中包含的私有API
    """
    bl_api, bl_class = api_dbs.get_black_list()
    api_names = [api['api_name'] for api in bl_api]
    file_strings = get_file_strings(file_name)
    matched_apis = []
    for s in file_strings:
        if s in api_names:
            matched_apis.append(s)
    return matched_apis


def find_private_classes(file_name):
    """
    搜索指定文件中包含的私有Class
    """
    bl_api, bl_class = api_dbs.get_black_list()
    class_names = [clz['class_name'] for clz in bl_class]
    file_strings = get_file_strings(file_name)
    matched_classes = []
    for s in file_strings:
        if s in class_names:
            matched_classes.append(s)
    return matched_classes


def print_usage():
    print('usage:\n\t python scan_file.py file_path')


def main():
    if len(sys.argv) != 2:
        print_usage()
        sys.exit()
    else:
        file_path = sys.argv[1]
        if not os.path.exists(file_path):
            print('指定文件不存在，请确认路径。')
            sys.exit()
        if os.path.isdir(file_path):
            print('请指定具体文件路径。')
            sys.exit()
        m_apis = find_private_apis(file_path)
        m_classes = find_private_classes(file_path)

        print('文件引用的私有API如下：')
        for api in m_apis:
            print(api)

        print('文件引用的私有class如下：')
        for clz in m_classes:
            print(clz)

if __name__ == '__main__':
    main()
