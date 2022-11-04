import json


# 获取JSON数组或对象的 key 列表
def get_json_keys(json_str, json_keys=[]):
    if isinstance(json_str, list):

        for json_obj in json_str:

            for key in json_obj.keys():

                if key not in json_keys:
                    json_keys.append(key)

    elif isinstance(json_str, dict):

        for key in json_str.keys():

            if key not in json_keys:
                json_keys.append(key)

    return json_keys


# 将JSON数组中相同的 key - value 值进行合并
def get_key_values(json_str, json_keys):
    target_json = {}

    for key in json_keys:

        key_values = []

        for json_obj in json_str:

            if isinstance(json_obj, dict):
                # 处理数组中，有些元素少了部分字段的情况
                try:
                    key_values.append(json_obj[key])
                except KeyError:
                    continue

                target_json[key] = key_values

    return target_json


# 主方法
def analyse_json(json_str):
    # 取出来的结果
    target_json = {}
    # 取出来的所有 key
    json_keys = []

    # 处理JSON数组的情况：
    # 1.取出所有的 key
    # 2.相同 key 的，value 放在同个列表里
    if isinstance(json_str, list):
        # 判断列表是不是JSON对象或数组之外的内容，如string列表，是则直接将列表作为 value 即可
        if not isinstance(json_str[0], list) and not isinstance(json_str[0], dict):
            target_json = json_str
        else:
            json_keys = get_json_keys(json_str, json_keys)
            target_json = get_key_values(json_str, json_keys)

    # 处理JSON对象的情况：
    # 1.取出所有的 key
    # 2.处理对应的 value ，直接加入结果集 or 递归调用继续处理JSON数组或对象
    elif isinstance(json_str, dict):
        json_keys = get_json_keys(json_str, json_keys)

        for key in json_keys:
            # 如果不是JSON数组或对象，就可以直接赋值了
            if not isinstance(json_str[key], list) and not isinstance(json_str[key], dict):
                target_json[key] = json_str[key]

            # 是JSON数组或对象的话，递归调用主方法，处理之
            else:
                target_json[key] = analyse_json(json_str[key])

    return target_json


if __name__ == '__main__':
    with open('apis.txt', 'r', encoding='utf-8') as f:
        json_str = f.read()
    result = analyse_json(json.loads(json_str))
    print(result)
