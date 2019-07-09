#!/usr/bin/bash
# coding:utf-8

# ==============================================================================
# File Name: feature.py
# Author: DaiDai
# Mail: daidai4269@aliyun.com
# Created Time: 一  4/29 12:22:22 2019
# ==============================================================================


# NOTE: testting code and check code style in linux and windows.

:<<!
# check OS type
sysOS=`uname -s`
flag="unix"

if [ $sysOS == "Darwin" ];then
    # Mac
    echo "Mac"
elif [ $sysOS == "Linux" ];then
    # linux
    echo "Linux"
else
    # win
    echo "Windows"
    flag="win"
fi


# TODO: not complete && code style will see google
# logtic
if [ $flag == "unix" ];then
    echo "unix"
    # flake8 
elif [ $flag == "win" ];then
    echo "win"
    # pyflakes.exe
fi
# gramma
if [ $flag == "unix" ];then
    echo "unix"
elif [ $flag == "win" ];then
    echo "win"
fi
!


# Python
# check code style and check error
pip install flake8
flake8 Python3.x/
# check variable type
pip install mypy
mypy Python3.x/
# C++
sudo apt-get install cppcheck  # static analysis tool for code
cppcheck C++/
pip install cpplint
cpplint C++/