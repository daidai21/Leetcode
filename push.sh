#!/bin/bash


python helper.py -r Algorithms/C
python helper.py -r Algorithms/C++
python helper.py -r Algorithms/Python3.x
python helper.py -r Concurrency/C
python helper.py -r Concurrency/C++
python helper.py -r Concurrency/Python3.x
git checkout test_case.py
git add .
git commit -m "."
git push origin master
