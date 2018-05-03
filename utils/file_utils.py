import os
import subprocess


def get_file_list(path, ext=None):
    """
    获取指定扩展名的文件列表
    """
    file_list = []
    get_all_files(path, file_list)
    if ext is None:
        return file_list
    else:
        return [f for f in file_list if os.path.basename(f).endswith(ext)]


def get_executable_file_list(path):
    """
    获取Payload中所有Match-O文件路径
    Match-O文件无扩展名……
    """
    cmd = u"python -mmacholib find %s" % (path)
    out = subprocess.check_output(cmd, shell=True)
    path_list = []
    if out:
        out = out.split()
        path_list = [x.decode('utf-8') for x in out]
        return path_list
    return False


def get_all_files(path, file_list):
    """
    获取给定目录下所有文件列表
    """
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            get_all_files(file_path, file_list)
        else:
            file_list.append(file_path)


def main():
    png_files = get_file_list('/Users/liyx/ios_check/ENTMOBILE-IOS_7.7.0_REVIEW6', 'png')   # noqa
    print(png_files)
    matcho_files = get_executable_file_list('/Users/liyx/ios_check/ENTMOBILE-IOS_7.7.0_REVIEW6')    # noqa
    print(matcho_files)


if __name__ == '__main__':
    main()
