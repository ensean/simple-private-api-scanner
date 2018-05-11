import os
import sys
import subprocess
from utils import file_utils


def file_contains_keyword(file_path, keyword):
    """
    判断指定文件strings是否包含特定关键词
    """
    cmd = 'strings %s | grep %s > /dev/null 2>&1' % (file_path, keyword)
    ret_code = os.system(cmd)
    return True if ret_code == 0 else False


def scan_keyword(path, ext, keyword):
    """
    在特定扩展名的文件中搜寻指定关键词，
    如在指定目录下所有.a文件中搜寻 UIStatusBar_Modern
    """
    if ext is None:
        file_list = file_utils.get_executable_file_list(path)
    else:
        file_list = file_utils.get_file_list(path, ext)
    matched_files = []
    for f in file_list:
        if file_contains_keyword(f, keyword):
            matched_files.append(f)
    return matched_files


def print_help():
    print("Usage python find_keyword.py target_dir [file_extension] keyword")


def main():
    if len(sys.argv) != 4 and len(sys.argv) != 3:
        print_help()
        sys.exit()
    else:
        path = sys.argv[1]
        if not os.path.exists(path):
            print('指定的文件目录不存在。')
            sys.exit()
        if len(sys.argv) == 4:
            ext = sys.argv[2]
            keyword = sys.argv[3]
        else:
            ext = None
            keyword = sys.argv[2]
        matched_files = scan_keyword(path, ext, keyword)
        print('在以下文件strings中匹配到关键词 %s' % keyword)
        for f in matched_files:
            print(f)

if __name__ == '__main__':
    main()
