from collections import defaultdict
import os
import sys


def get_dublicate_files(path_to_folder):
    dublicate_files = defaultdict(list)
    all_files = {}
    for dir_path, dir_names, file_names in os.walk(path_to_folder):
        for file_name in file_names:
            path_to_file = os.path.join(dir_path, file_name)
            size_file = os.stat(path_to_file).st_size
            if all_files.get(file_name) and all_files[file_name] == size_file:
                dublicate_files[(file_name, size_file)] = path_to_file
            else:
                all_files[file_name] = size_file

    return dublicate_files


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Не указана папка')

    path_to_folder = sys.argv[1]
    dublicate_files = get_dublicate_files(path_to_folder)
    for file_info, file_path in dublicate_files.items():
        print(file_path, file_info[1])
