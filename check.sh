#!/usr/bin/bash
# coding:utf-8

# ==============================================================================
# File Name: check.sh
# Author: DaiDai
# Mail: daidai4269@aliyun.com
# Created Time: 一  4/29 12:22:22 2019
# ==============================================================================


# Python
echo "===== check Python code style and check error"
pip install flake8
flake8 Algorithms/Python3.x/
echo "===== check Python variable type"
pip install mypy
mypy Algorithms/Python3.x/
# C++
sudo apt-get install cppcheck
echo "===== static analysis C++ code"
cppcheck Algorithms/C++/
pip install cpplint
echo "===== code typle C++ code"
find Algorithms/C++/ | xargs cpplint
