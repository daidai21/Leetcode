#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# =============================================================================
# File Name: helper.py
# Author: DaiDai
# Mail: daidai4269@aliyun.com
# Created Time: Thu Aug 15 17:50:36 2019
# =============================================================================


import os
import copy
import argparse
import pandas as pd


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
    file_list = os.listdir(dir_path)

    all_lines = 0
    for file_name in file_list:
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, "rb") as file:
            all_lines += len(file.readlines())
    print("path: {0} \t All lines: {1}".format(dir_path, all_lines))


def see_not_over_problem(dir_name):
    """
    see have not over problem in frequency sorted
    """
    problem_df = pd.read_csv("problem.csv")
    del_idx = problem_df[(192 <= problem_df["id"]) & 
                         (problem_df["id"] <= 195)].index.tolist()  # bash problem
    problem_df.drop(del_idx, axis=0, inplace=True)
    problem_df.sort_values(by="frequency", inplace=True, ascending=True)
    code_filename_list = os.listdir(dir_name)

    not_over_list = []
    for _, problem in problem_df.iterrows():
        idx = str(problem["id"]) + "-"
        len_idx = len(idx)
        over = False
        for filename in code_filename_list:
            if idx == filename[:len_idx]:
                print("over: ", filename)
                over = True
        if not over:
            if problem["vip"] != "Prime":
                not_over_list.append((
                    problem["id"], 
                    problem["title"], 
                    problem["difficulty"], 
                    problem["frequency"]
                ))

    print("num \t id \t difficulty \t frequency \t problem")
    for idx, not_over in enumerate(not_over_list):
        print("{0} \t {1: >4d} \t {2:<6s} \t {3:.2f} \t {4}".format(
            idx, not_over[0], not_over[2], not_over[3], not_over[1]
        ))
    print("\n over num: {0}, not over num: {1}".format(
        problem_df.shape[0] - len(not_over_list), 
        len(not_over_list))
    )

    return not_over_list


def command():
    """
    command define
    """
    description="help script."
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("-py", "--python", action="store_true", help="Python")
    parser.add_argument("-cc", "--cpp", action="store_true", help="C++")

    parser.add_argument("-r", "--rename", action="store_true", help="rename")
    parser.add_argument("-l", "--lines", action="store_true", help="see all code lines")
    parser.add_argument("-t", "--todo", action="store_true", help="see not over problem")

    args = parser.parse_args()
    if args.python:
        if args.rename:
            rename("./Python3.x")
        if args.lines:
            see_all_code_lines("./Python3.x/")
        if args.todo:
            see_not_over_problem("Python3.x/")
    elif args.cpp:
        if args.rename:
            rename("./C++")
        if args.lines:
            see_all_code_lines("./C++/")
        if args.todo:
            see_not_over_problem("C++/")
    else:
        os.system("python {0} --help".format(__file__))


if __name__ == "__main__":
    command()
