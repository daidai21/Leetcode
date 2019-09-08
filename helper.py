#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# =============================================================================
# File Name: helper.py
# Author: DaiDai
# Mail: daidai4269@aliyun.com
# Created Time: Thu Aug 15 17:50:36 2019
# =============================================================================


import os
import sys
import copy
import argparse
import pandas as pd


def file_rename(dir_path):
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        new_file_name_list = file_name.split(" ")
        if len(new_file_name_list) == 1:
            pass
        else:
            new_file_name = new_file_name_list[0][:-1] + "-" + '_'.join(new_file_name_list[1:])
            os.rename(file_path, os.path.join(dir_path, new_file_name))


def statistics_file_lines(dir_path):
    all_lines = 0
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, "rb") as file:
            all_lines += len(file.readlines())
    print("Path: {0} \t Lines: {1}".format(dir_path, all_lines))


def see_not_over_problem(dir_name):
    """
    see have not over problem in frequency sorted
    """
    try:
        problem_df = pd.read_csv("problem.csv")
    except Exception as err:
        print(err)
        sys.exit(0)
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
    parser = argparse.ArgumentParser(description="help script.")

    parser.add_argument("-r", "--rename", action="store", type=str, help="file rename")
    parser.add_argument("-l", "--lines", action="store", type=str, help="statistics file lines")
    parser.add_argument("-t", "--todo", action="store", type=str, help="see not over problem")

    args = parser.parse_args()
    if args.rename:
        file_rename(args.rename)
    elif args.lines:
        statistics_file_lines(args.lines)
    elif args.todo:
        see_not_over_problem(args.todo)
    else:
        os.system("python {0} --help".format(__file__))


if __name__ == "__main__":
    command()
