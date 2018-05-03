# coding=utf-8
from utils.sqlite_utils import SqliteHandler


def get_black_list(framework=None):
    """
    获取API黑名单、Class Name黑名单、禁用Framework、高危Framework
    """
    # 获取non-public api列表
    sql_api = "select distinct(api_name) from blacklist where api_name not in (select distinct(api_name) from whitelist where api_name is not null);"   # noqa
    sql_class = "select distinct(class_name) from blacklist where class_name not in (select distinct(class_name) from whitelist where class_name is not null);"     # noqa
    params = ()
    api_black_list = SqliteHandler().exec_select(sql_api, params)
    class_black_list = SqliteHandler().exec_select(sql_class, params)
    return api_black_list, class_black_list


def enrich_class_info(class_list, target='private'):
    """
    补充class的framework信息
    """
    new_class_list = []
    for c in class_list:
        if c:
            framework = _get_private_framework_by_class(
                c['class_name'], target)
            if framework:
                c['framework'] = framework['framework']
            else:
                c['framework'] = None
            if 'type' in framework.keys():
                c['type'] = framework['type']
            else:
                c['type'] = target
            new_class_list.append(c)
    return new_class_list


def _get_private_framework_by_class(class_name, target='private'):
    """
    根据class名称获取framework名
    """
    class_name = class_name.strip()
    # 构建 ios_private.db时使用
    sql = ""
    if target == 'private':
        sql = "select framework from private_framework_dump_apis where class_name='%s' and framework is not null;" % class_name     # noqa
    elif target == 'undocument':
        sql = "select framework from framework_dump_apis where class_name='%s' and framework is not null;" % class_name     # noqa
    elif target == 'blacklist':  # 检测ipa时使用
        sql = "select header_file as framework, type from blacklist where class_name='%s';" % class_name    # noqa
    else:
        pass
    return SqliteHandler().exec_select_one(sql, ())


def get_private_framework_dump_apis(sdk):
    sql = "select * from private_framework_dump_apis where sdk = ?"
    params = (sdk, )
    return SqliteHandler().exec_select(sql, params)


def get_framework_dump_apis(sdk):
    sql = "select * from framework_dump_apis where sdk = ?"
    params = (sdk, )
    return SqliteHandler().exec_select(sql, params)


def get_framework_private_apis():
    sql = "select * from framework_private_apis group by api_name;"
    params = ()
    return SqliteHandler().exec_select(sql, params)


def is_api_exist_in(table_name, api):
    sql = "select * from " + table_name + \
        " where api_name = ? and class_name = ? and sdk = ?;"
    params = (api['api_name'], api['class_name'], api['sdk'])
    return SqliteHandler().exec_select_one(sql, params)