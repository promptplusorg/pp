def get_file_list():

    import os
    import datetime

    folder_path = '/kim/pp/sandbox'
    file_list = os.listdir(folder_path)

    file_info_list = []

    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            file_stat = os.stat(file_path)
            modified_time = datetime.datetime.fromtimestamp(file_stat.st_mtime)
            file_size = file_stat.st_size
            file_info = {
                'name': file_name,
                'modifiedTime': modified_time,
                'size': file_size
            }
            file_info_list.append(file_info)

    print(file_info_list)

    return file_info_list
