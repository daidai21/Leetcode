#!/usr/bin/python3
import os
import copy


def rename(dir_path):
    '''
    change " " to "_" in dir_path
    '''
    file_list = os.listdir(dir_path)
    for file_name in file_list:
        file_path = os.path.join(dir_path, file_name)
        new_file_path = os.path.join(dir_path, '_'.join(file_name.split(" ")))
        os.rename(file_path, new_file_path)


def see_all_code_lines(dir_path):
    '''
    see all code lines in dir_path
    '''
    print(dir_path)
    file_list = os.listdir(dir_path)

    all_lines = 0
    for file_name in file_list:
        file_path = os.path.join(dir_path, file_name)
        output = os.popen("wc -l " + file_path)
        # print(output.read().split(' '))
        try:
            all_lines += int(output.read().split(' ')[0])
        except Exception as err:
            print("Error: ", file_path)
    print("all_lines: ", all_lines)


if __name__ == "__main__":
    rename("./Python3.x")
    rename("./C++")

    see_all_code_lines("./Python3.x/")
    see_all_code_lines("./C++/")

