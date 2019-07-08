import os
import copy


def rename(dir_path):
    '''
    change " " to "_" in dir_path
    '''
    file_list = os.listdir(dir_path)
    for file_name in file_list:
        file_path = os.path.join(dir_path, file_name)
        new_file_path = ""
        for c in file_path:
            if c == " ":
                new_file_path += "_"
            else:
                new_file_path += c
        os.rename(file_path, new_file_path)


if __name__ == "__main__":
    # rename Python file ()
    rename("./Python3.x")
    # rename Python file ()
    rename("./C++")
