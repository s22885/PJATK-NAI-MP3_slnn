import os


def get_langs(dir_path: str = "data"):
    tmp_files_op = os.listdir(dir_path)
    res = []
    for i in tmp_files_op:
        if os.path.isdir(dir_path + "/" + i):
            res.append(i)
    return res


def get_file_names(lang_list: list, dir_path: str = "data"):
    res = []
    for dir_lang in lang_list:
        tmp_path = dir_path + "/" + dir_lang
        tmp_files_op = os.listdir(tmp_path)
        for file_in in tmp_files_op:
            tmp_path_file = tmp_path + "/" + file_in
            if os.path.isfile(tmp_path_file):
                res.append([dir_lang, tmp_path_file])
    return res
